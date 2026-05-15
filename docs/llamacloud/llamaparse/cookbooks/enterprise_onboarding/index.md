---
title: Enterprise Rollout | Developer Documentation
---

## **Overview**

Rolling out LlamaCloud in a large enterprise requires planning to ensure a seamless onboarding experience for users. This guide provides step-by-step instructions for configuring LlamaCloud for an enterprise environment, defining user roles, setting up integrations, and best practices for operationalizing LlamaCloud in production.

Note that we will be expanding our RBAC offerings, and this cookbook will evolve with additional features

## **Step 1: Setting Up Your Organization**

LlamaCloud structures access and resources using **Organizations** and **Projects**.

### **1.1 Create a Central Organization**

- Navigate to **Settings**
- Define a single **organization** for your enterprise (e.g., ACME instead of each user having their own organization).
- As you scale, you can consider additional organizations. We have seen large enterprises create an organization per business unit.

### **1.2 Configure Projects for Departments/ Teams**

Each **Project** serves as a logical unit within the organization. Recommended structure:

- **Experiments**: For initial testing and onboarding
- **Teams**: Create dedicated projects per Team (e.g., Research, Engineering).

Note that integrations are scoped to a project (see below).

## **Step 2: Setting Up Integrations**

You can pre-configure integrations to streamline workflows for your users. There are 3 kinds of integrations

- Embedding Model (e.g. OpenAI keys)
- Data Sink (e.g. vectorDB like MongoDB)
- Data Source (e.g. Sharepoint or Box)

### **2.1 Configuring Embedding Models**

- **Embedding model API Key Management**: Configure Embedding Model connection as a shared project resource. When creating an Index, a user can select from a dropdown the already configured API key instead of entering credentials manually.

### **2.2 Data Sources and Data Sinks**

- **Pre-configure Data Source Connectors**: Use a service credential to provide controlled access to shared folders.
- Pre-Configure Data Sink Connection
- When creating an index, users can select Data Source and Data Sink from a dropdown list

## **Step 3: Defining Users and Roles**

In Settings → Members you can add team members to your organization. By default, LlamaCloud has two roles: **Admin** and **Viewer**. We plan to add additional roles for granular control.

## **Step 4: Enterprise Rollout Strategy**

### **4.1 Phase 1: Pilot Group Deployment**

- Start with a small team of **10-25 pilot users** in the `Experiments` project.
- Gather feedback on usability, security, and role assignments.

### **4.2 Phase 2: Teams Expansion**

- Roll out LlamaCloud to various teams (or use cases) by creating projects for each.
- Configure resources for each project so that the Index creation process is seamless
