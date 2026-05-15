---
title: Multi-Environments | Developer Documentation
---

## Single Project Approach

Keep all three environments (dev, UAT, production) in the same project.

**Benefits:**

- **Easy management** - Everything in one place
- **Quick setup** - Use “Duplicate” button to copy between environments
- **Streamlined workflow** - Promote changes from dev → UAT → prod seamlessly

**How to set up:**

1. Create one project for your application
2. Name your indexes with environment prefixes: `dev-products`, `uat-products`, `prod-products`
3. Use the duplicate feature to copy indexes configuration (“Duplicate” button can be found in the index page).

## Alternative: Separate Projects

Create individual projects for each environment (3 projects total).

**Consider this only if:**

- You have specific organizational requirements for complete separation

**Important considerations:**

- **Manual synchronization** - No easy way to copy configurations between projects

## Our Recommendation

Start with the single project approach. It’s simpler, more cost-effective, and easier to manage. You can always separate later if your needs change.

## Need Help?

Contact us if you have questions about setting up your environments.
