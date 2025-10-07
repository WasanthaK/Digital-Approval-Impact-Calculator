# Digital Approval Impact Calculator

A tool to calculate the environmental and operational impact of transitioning to digital approvals and sealing.

## Overview

This calculator helps organizations understand the sustainability benefits and cost savings achieved by moving from paper-based to digital approval processes.

## Methodology & Data Sources

Our calculations are based on peer-reviewed research and data from reputable environmental organizations:

### Carbon Emissions (CO₂)
- **Value:** 4.71 grams CO₂ per sheet
- **Source:** Environmental Paper Network (2018) - "The State of the Global Paper Industry"
- **Explanation:** This includes emissions from paper production, transportation, and disposal

### Trees Saved
- **Value:** 8,333 sheets per tree
- **Source:** Conservatree.org and forestry industry data
- **Explanation:** Based on average office paper production from a single tree. This varies depending on tree species (e.g., pine, fir, spruce) and paper type (e.g., office paper vs. newsprint)

### Water Conservation
- **Value:** 10 liters per sheet
- **Source:** WWF (World Wildlife Fund) paper production studies
- **Explanation:** Includes water used in pulp processing and paper manufacturing. The paper industry is one of the largest industrial water consumers

### Energy Savings
- **Value:** 0.5 kWh per sheet
- **Source:** EPA Energy Star Program data
- **Explanation:** Covers energy for production, printing, and distribution of paper documents

### Cost Savings
- **Paper Cost:** $0.05 per sheet (average commercial paper cost)
- **Mailing Cost:** $0.50 per document (postage and handling estimate)
- **Source:** Industry averages for commercial paper purchasing and postal services

## Sustainable Development Goals (SDGs)

This tool highlights contributions to the following UN Sustainable Development Goals:

- **SDG 6 (Clean Water and Sanitation):** Reducing water consumption in paper production
- **SDG 7 (Affordable and Clean Energy):** Decreasing energy use in manufacturing and distribution
- **SDG 13 (Climate Action):** Lowering CO₂ emissions and combating climate change
- **SDG 15 (Life on Land):** Preserving forests and protecting biodiversity

## Important Disclaimer

**These are estimates based on industry averages.** Actual environmental impacts may vary depending on:

- Paper type and quality (recycled vs. virgin paper, weight, etc.)
- Manufacturing processes and technology used
- Regional differences in energy sources and water availability
- Transportation distances and methods
- End-of-life disposal methods (recycling, landfill, incineration)

## References

1. **Environmental Paper Network** - [www.environmentalpaper.org](https://www.environmentalpaper.org)
   - Comprehensive reports on the environmental impact of paper production

2. **Conservatree** - [www.conservatree.org](https://www.conservatree.org)
   - Environmental impact statistics and paper consumption data

3. **World Wildlife Fund (WWF)** - [www.worldwildlife.org](https://www.worldwildlife.org)
   - Paper consumption and water usage research

4. **EPA Energy Star Program** - [www.energystar.gov](https://www.energystar.gov)
   - Energy efficiency data for paper production

## Usage

### Web Version (index.html)
Open `index.html` in any modern web browser. Enter your annual document volumes and click "Calculate Impact" to see results.

### Python/Streamlit Version (calculate.py)
```bash
pip install streamlit pillow
streamlit run calculate.py
```

## Features

- Real-time impact calculations
- Visual representation of sustainability metrics
- Downloadable reports (Markdown, Image, Word)
- Social sharing capabilities
- UN SDG alignment tracking

## Contributing

Contributions are welcome! If you have updated research or more accurate data sources, please submit a pull request with:
- Updated values
- Source citations
- Explanation of changes

## License

This tool is provided for educational and informational purposes. The methodology and sources are transparent to allow for verification and improvement.
