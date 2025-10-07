#!/bin/bash
# Branch Cleanup Script for Digital Approval Impact Calculator
# This script will delete the old copilot branches that have been merged

echo "=================================="
echo "Branch Cleanup Script"
echo "=================================="
echo ""

# Check if we're in a git repository
if [ ! -d .git ]; then
    echo "❌ Error: Not in a git repository"
    exit 1
fi

echo "This script will delete the following branches:"
echo "  1. copilot/fix-de758515-2233-410a-b2b2-b21c1b87e309 (already merged in PR #1)"
echo "  2. copilot/fix-7662c785-67ac-4a17-a0f2-82f461a1fd9b (merged in this PR)"
echo ""

read -p "Do you want to continue? (y/N) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 0
fi

echo ""
echo "Deleting remote branches..."
echo ""

# Delete the first copilot branch
echo "🗑️  Deleting copilot/fix-de758515-2233-410a-b2b2-b21c1b87e309..."
git push origin --delete copilot/fix-de758515-2233-410a-b2b2-b21c1b87e309 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Successfully deleted copilot/fix-de758515-2233-410a-b2b2-b21c1b87e309"
else
    echo "⚠️  Could not delete copilot/fix-de758515-2233-410a-b2b2-b21c1b87e309 (may already be deleted)"
fi

echo ""

# Delete the second copilot branch
echo "🗑️  Deleting copilot/fix-7662c785-67ac-4a17-a0f2-82f461a1fd9b..."
git push origin --delete copilot/fix-7662c785-67ac-4a17-a0f2-82f461a1fd9b 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Successfully deleted copilot/fix-7662c785-67ac-4a17-a0f2-82f461a1fd9b"
else
    echo "⚠️  Could not delete copilot/fix-7662c785-67ac-4a17-a0f2-82f461a1fd9b (may already be deleted)"
fi

echo ""
echo "Cleaning up local references..."
git fetch --prune

echo ""
echo "=================================="
echo "✅ Cleanup complete!"
echo "=================================="
echo ""
echo "Remaining branches:"
git branch -r | grep -v "HEAD"
echo ""
echo "You should now only have origin/main listed above."
