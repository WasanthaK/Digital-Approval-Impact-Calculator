import streamlit as st
from PIL import Image
import io
import urllib.parse

# Constants - Based on industry research and environmental studies
# Sources:
# - CO2: Environmental Paper Network (2018) - "The State of the Global Paper Industry"
# - Trees: Conservatree.org - Average of 8,333 sheets per tree (varies by tree type)
# - Water: WWF (World Wildlife Fund) - Paper production water consumption data
# - Energy: EPA Energy Star Program - Average energy for paper production
CO2_PER_SHEET = 0.00471  # kg CO2 per sheet (4.71 grams)
SHEETS_PER_TREE = 8333   # sheets per tree (based on average office paper production)
WATER_PER_SHEET = 10     # liters of water per sheet (paper manufacturing process)
PAPER_COST_PER_SHEET = 0.05  # USD per sheet (average commercial paper cost)
MAIL_COST_PER_DOC = 0.50  # USD per document (postage and handling estimate)
ENERGY_PER_SHEET = 0.5  # kWh energy saved per sheet (production and distribution)

# Function to generate results as Markdown
def generate_results_md(carbon_saved, trees_saved, water_saved, energy_saved, total_savings):
    return f"""
    ## Our Contribution to Sustainability

    - **Carbon Saved:** {carbon_saved:.2f} kg of CO₂  
    - **Trees Saved:** {trees_saved:.2f}  
    - **Water Saved:** {water_saved:.0f} liters  
    - **Energy Saved:** {energy_saved:.2f} kWh  
    - **Cost Savings:** ${total_savings:.2f}  

    ### SDG Contributions
    - **SDG 6 (Clean Water):** Conserved {water_saved:.0f} liters of water.  
    - **SDG 7 (Affordable and Clean Energy):** Saved {energy_saved:.2f} kWh of energy.  
    - **SDG 13 (Climate Action):** Avoided {carbon_saved:.2f} kg of CO₂ emissions.  
    - **SDG 15 (Life on Land):** Preserved {trees_saved:.2f} trees.  
    
    ---
    
    ### Methodology
    Calculations based on industry research from Environmental Paper Network, WWF, EPA Energy Star, and Conservatree.org.
    These are estimates based on industry averages. Actual impacts may vary.
    """

# Streamlit App
st.set_page_config(page_title="Digital Approval Impact Calculator", layout="centered")
st.title("🌍 Digital Approval Impact Calculator")
st.write("""
This tool calculates the environmental and operational impact of transitioning 
to digital approvals and sealing.
""")

# Add methodology information
with st.expander("📚 Methodology & Data Sources"):
    st.markdown("""
    ### How We Calculate Environmental Impact
    
    Our calculations are based on industry research and environmental studies:
    
    **Carbon Emissions (CO₂):**
    - **Value:** 4.71 grams CO₂ per sheet
    - **Source:** Environmental Paper Network (2018) - "The State of the Global Paper Industry"
    - Paper production, transportation, and disposal contribute to carbon emissions
    
    **Trees Saved:**
    - **Value:** 8,333 sheets per tree
    - **Source:** Conservatree.org and forestry industry data
    - Based on average office paper production from a single tree
    - Varies depending on tree species and paper type
    
    **Water Conservation:**
    - **Value:** 10 liters per sheet
    - **Source:** WWF (World Wildlife Fund) paper production studies
    - Includes water used in pulp processing and paper manufacturing
    
    **Energy Savings:**
    - **Value:** 0.5 kWh per sheet
    - **Source:** EPA Energy Star Program data
    - Covers energy for production, printing, and distribution
    
    **Cost Savings:**
    - Paper cost: $0.05 per sheet (commercial average)
    - Mailing cost: $0.50 per document (postage and handling)
    
    ### Disclaimer
    These are estimates based on industry averages. Actual impacts may vary depending on:
    - Paper type and quality
    - Manufacturing processes
    - Regional differences
    - Distribution methods
    
    ### References
    - Environmental Paper Network: [www.environmentalpaper.org](https://www.environmentalpaper.org)
    - Conservatree: [www.conservatree.org](https://www.conservatree.org)
    - WWF Paper Calculator: [www.worldwildlife.org](https://www.worldwildlife.org)
    - EPA Energy Star: [www.energystar.gov](https://www.energystar.gov)
    """)


# Input Section
st.header("📊 Enter Your Data")
doc_volume = st.number_input("Total Documents Produced Annually", min_value=0, step=1)
signed_docs = st.number_input("Documents Needing Signature and Seal", min_value=0, step=1)

if st.button("Calculate Impact"):
    if doc_volume == 0 or signed_docs == 0:
        st.warning("Please enter valid values for both fields.")
    else:
        # Calculations
        carbon_saved = signed_docs * CO2_PER_SHEET  # kg CO2
        trees_saved = signed_docs / SHEETS_PER_TREE  # Trees
        water_saved = signed_docs * WATER_PER_SHEET  # Liters
        energy_saved = signed_docs * ENERGY_PER_SHEET  # kWh
        total_savings = signed_docs * PAPER_COST_PER_SHEET + signed_docs * MAIL_COST_PER_DOC  # USD

        # Results Section
        st.header("🌱 Our Contribution to Sustainability")
        col1, col2, col3, col4, col5  = st.columns(5)
        col1.image("https://via.placeholder.com/80/3498db/ffffff?text=CO2", caption="Carbon Saved", use_container_width=True)
        col1.metric("Carbon Saved (kg)", f"{carbon_saved:.2f}")
        
        col2.image("https://via.placeholder.com/80/2ecc71/ffffff?text=Tree", caption="Trees Saved", use_container_width=True)
        col2.metric("Trees Saved", f"{trees_saved:.2f}")
        
        col3.image("https://via.placeholder.com/80/f1c40f/ffffff?text=Water", caption="Water Saved", use_container_width=True)
        col3.metric("Water Saved (L)", f"{water_saved:.0f}")

        col4.image("https://via.placeholder.com/80/f39c12/ffffff?text=Energy", caption="Energy Saved", use_container_width=True)
        col4.metric("Energy Saved (kWh)", f"{energy_saved:.2f}")
        
        col5.image("https://via.placeholder.com/80/e74c3c/ffffff?text=$", caption="Cost Savings", use_container_width=True)
        col5.metric("Cost Savings (USD)", f"${total_savings:.2f}")

        # SDG Contributions
        st.subheader("📈 SDG Contributions")
        st.markdown(f"""
        - **SDG 6 (Clean Water):** Conserved {water_saved:.0f} liters of water.  
        - **SDG 7 (Affordable and Clean Energy):** Saved {energy_saved:.2f} kWh of energy.  
        - **SDG 13 (Climate Action):** Avoided {carbon_saved:.2f} kg of CO₂ emissions.  
        - **SDG 15 (Life on Land):** Preserved {trees_saved:.2f} trees.  
        """)

        # Download Results as Markdown
        results_md = generate_results_md(carbon_saved, trees_saved, water_saved, energy_saved, total_savings)
        st.download_button("📅 Download Results as Markdown", data=results_md, file_name="sustainability_report.md", mime="text/markdown")

        # Social Sharing Section
        st.subheader("📢 Share Your Impact")
        share_text = f"By using digital signatures with {signed_docs} documents, I just saved {carbon_saved:.2f} kg of CO2, preserved {trees_saved:.2f} trees, conserved {water_saved:.0f} liters of water, and saved {energy_saved:.2f} kWh of energy. Join the movement for sustainability! Calculated by Evia Sign Savings calculator #eviasign"
        twitter_url = f"https://twitter.com/intent/tweet?{urllib.parse.urlencode({'text': share_text})}"
        linkedin_url = f"https://www.linkedin.com/shareArticle?{urllib.parse.urlencode({'mini': 'true', 'title': 'Sustainability Impact', 'summary': share_text, 'source': 'https://yourappurl.com'})}"
        facebook_url = f"https://www.facebook.com/sharer/sharer.php?{urllib.parse.urlencode({'u': 'https://yourappurl.com', 'quote': share_text})}"

        st.markdown(f"[Share on Twitter]({twitter_url}) 💓")
        st.markdown(f"[Share on LinkedIn]({linkedin_url}) 🔗")
        st.markdown(f"[Share on Facebook]({facebook_url}) 👍")
