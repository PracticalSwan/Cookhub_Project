# Recipe Sharing System

A collaborative web application that enables users to share, discover, and interact with recipes. The system features role-based access for Admins, Contributors, and regular Users, with a robust recipe approval workflow and comprehensive recipe management capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [User Roles & Functions](#user-roles-functions)
  - [Admin Dashboard](#admin-dashboard)
  - [User (Contributor) Module](#user-contributor-module)
  - [User (Guest) Module](#user-guest-module)
- [Installation & Setup](#installation-setup)
- [Available Scripts](#available-scripts)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [System Diagrams](#system-diagrams)
- [Data Storage](#data-storage)
- [Support](#support)

<a id="overview"></a>
## 🎯 Overview

The Recipe Sharing System is built to facilitate a community-driven platform where:
- **Guests (Pending Users)** - New registrations start with pending status; can browse and search recipes while awaiting admin approval
- **Contributors (Active Users)** - Approved users with full platform access; create and manage recipes, interact with content through likes/favorites/reviews
- **Admins** - Oversee the platform with user activation, recipe approval workflows, analytics, and content moderation

The system features a **comprehensive approval workflow** where:
1. New users register → Account created with "Pending" status
2. Admin reviews and activates user accounts
3. Contributors submit recipes → Admin approves before publication
4. Activity tracking and analytics provide insights into platform engagement

The system uses a **client-side storage approach** with localStorage, making it lightweight and suitable for demonstration and development purposes.

<a id="key-features"></a>
## ✨ Key Features

### Core Functionality
- ✅ User authentication with role-based access control (Admin, Contributor, User)
- ✅ Recipe submission with admin approval workflow
- ✅ Comprehensive recipe management (Create, Read, Update, Delete)
- ✅ Advanced recipe discovery (search, filtering, sorting)
- ✅ User profile management
- ✅ Recipe ratings and reviews (one review per user per recipe)
- ✅ Favorites/saved recipes functionality
- ✅ Interactive ingredient checklist to mark off ingredients while cooking
- ✅ Admin dashboard with site analytics and metrics
- ✅ User and recipe management tools for admins
- ✅ Activity tracking system with real-time updates
- ✅ Last active timestamp tracking (updated on logout/browser close)
- ✅ Daily Active Users (DAU) tracking with session heartbeat
- ✅ Admin activity logging (user/recipe management actions)

<a id="system-architecture"></a>
## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                        Recipe Sharing System                                 │
├──────────────────────────────────────────────────────────────────────────────┤
│  Authentication & Authorization (Login Required)                             │
│  ├── Registration → Initial Status: Pending                                  │
│  └── Role-based Access Control (Admin, Contributor, Guest)                   │
├──────────────────────────────────────────────────────────────────────────────┤
│  Admin Module             Contributor Module         Guest Module (Pending)  │
│  ├── Dashboard            ├── Full Platform Access   ├── Browse Recipes      │
│  ├── User Management      ├── Create Recipe          ├── Search & Filter     │
│  ├── Recipe Approval      ├── My Recipes             ├── View Recipe Details │
│  ├── Analytics & Stats    ├── Profile Management     ├── View Reviews        │
│  └── Activity Logs        ├── Favorites              └── Awaits Admin        │
│                           ├── Reviews & Ratings          Approval for        │
│                           └── Likes & Engagement         Full Access         │
├──────────────────────────────────────────────────────────────────────────────┤
│  Data Layer: Local Storage                                                   │
│  ├── User Accounts (credentials, profiles, roles, status)                    │
│  ├── Recipes (content, status, metadata)                                     │
│  ├── Reviews & Ratings (one per user per recipe)                             │
│  ├── Daily Stats (views, active users, new users)                            │
│  └── Activity Logs (admin actions, user management)                          │
└──────────────────────────────────────────────────────────────────────────────┘
```

<a id="user-roles-functions"></a>
## 👥 User Roles & Functions

<a id="admin-dashboard"></a>
### Admin Dashboard

**Access:** Login with admin credentials (`admin@example.com` / `password`)

#### 1. **Dashboard & Analytics**
- View real-time metrics and site-wide analytics
- Track daily activity and user engagement
- **Recent Activity Feed:** Dynamic log showing latest admin actions (user status changes, recipe approvals/rejections, account deletions)

**Metrics Displayed:**
| Metric | Description |
|--------|-------------|
| Total Users | Total number of registered users |
| New Users | Number of new users registered today |
| Total Contributors | Total number of users with contributor role |
| New Contributors | Number of new contributors registered today |
| Total Published Recipes | Count of approved and visible recipes |
| Total Pending Recipes | Count of recipes awaiting approval |
| Daily Views | Site-wide page views per day |
| Daily Active Users (DAU) | Number of unique active users per day (with hourly heartbeat tracking) |

#### 2. **User Management**
- View a comprehensive list of all registered users in table format
- Display user details including:
  - Username
  - Email address
  - Account status (Active, Inactive, Pending, Suspended)
  - User role (Admin, Contributor, User)
  - Account creation date
  - Last activity timestamp (auto-updates on logout/browser close)
- Activate or deactivate user accounts (logs admin action)
- Delete user accounts from the system (logs admin action)

#### 3. **Recipe Management**
- **Recipe Approval Workflow:**
  - View all recipes (Pending, Approved, Rejected)
  - Approve pending recipes to make them visible to users (logs admin action)
  - Reject recipes (logs admin action)
  - Delete any recipe from the system with modal confirmation (auto-removes from all user favorites)
  - Preview complete recipe details (ingredients, instructions, contributor info)

**Recipe Management Table Displays:**
- Recipe ID
- Recipe title
- Recipe image thumbnail
- Contributor name
- Current status (Pending, Approved, Rejected)
- Created date
- Action buttons (View, Approve, Reject, Delete)

---

<a id="user-contributor-module"></a>
### User (Contributor) Module

**Access:** Registration + Login as a Contributor (full feature access)

#### 1. **Authentication**
- **Registration:** Create account with:
  - First name & last name
  - Email address
  - Birthday
  - Password (with confirmation)
- **Login:** Email and password authentication
- **Logout:** Secure session termination

#### 2. **Profile Management**
Edit and manage your contributor profile with:
- Full name
- Bio/About section
- Avatar image
- Location
- Email address
- Cooking skill level (Beginner, Intermediate, Advanced)

#### 3. **Create Recipe**
Submit new recipes with comprehensive details:
- **Recipe Image:** Upload or link recipe photo
- **Title:** Recipe name
- **Description:** Detailed overview of the dish
- **Categories:** Select 1–3 recipe tags (e.g., Breakfast, Dinner, Dessert)
- **Duration:** Prep time and cook time
- **Servings:** Number of people the recipe serves
- **Difficulty:** Easy, Medium, or Hard
- **Instructions:** Step-by-step cooking instructions
- **Ingredients:** List with name, quantity, and measurement unit

**Important:** Recipes remain **hidden** until approved by an admin

#### 4. **My Recipes**
- View all your submitted recipes with their current approval status
- **Edit recipes:** Modify any of your submitted recipes
- **Delete recipes:** Remove recipes from the system
- Track approval status of each recipe (Pending, Approved, Rejected)

#### 5. **Discover & Browse Recipes**
- View all approved recipes from the community
 - See recipe details including images, descriptions, ingredients (with interactive checklist), and instructions
- Explore recipes from various contributors

#### 6. **Search & Filter**
- Keyword search across recipe titles
- Real-time search results with URL persistence
- **Search History:** Automatic logging of your search queries with timestamps
  - View your recent searches
  - Clear search history with one click
- Filter by category/tags and difficulty level (category filter matches any selected tag)
- **Reset Filters:** Quickly reset all filters to default values
- Sort by newest recipes, most liked recipes (Most Popular - default), or difficulty level
- **Smart Filter Persistence:** Filters remain active when changing search keywords

#### 7. **Saved Recipes (Favorites)**
- Save recipes to your personal collection
- View all saved recipes in one place
- Remove recipes from your saved list
- Quick access to favorite recipes for future reference

#### 8. **Reviews & Ratings**
- **Rate recipes** on a 1-5 star scale
- **Write reviews:** Submit detailed text reviews with your thoughts (one review per recipe)
- **Update reviews:** Edit your existing review on a recipe
- **View community ratings:** See average ratings and other user reviews
- **Delete your reviews:** Remove your own reviews anytime
- Contribute to recipe ratings that help the community discover great recipes

#### 9. **Engagement Features**
- **Like recipes:** Show appreciation for recipes you enjoy
- **View counts:** Track how many people viewed recipes
- **Recipe views:** See which recipes are most popular

---

<a id="user-guest-module"></a>
### User (Guest) Module

**Access:** Registration + Login as a Guest (Pending Status)

**Status:** New users register as guests with Pending status and await admin approval to become Active

#### 1. **Authentication**
- **Registration:** Create account with:
  - First name & last name
  - Email address
  - Birthday
  - Password (with confirmation)
- **Initial Status:** Account created as "Pending" - awaiting admin activation
- **Login:** Email and password authentication
- **Logout:** Secure session termination

#### 2. **Discover & Browse Recipes**
- View all approved recipes from the community
- See recipe details including images, descriptions, ingredients, and instructions
- Explore recipes from various contributors

#### 3. **Search & Filter**
**Search Functionality:**
- Keyword search across recipe titles
- Real-time search results with URL persistence
- **Search History:** Automatic logging of your search queries with timestamps
  - View your recent searches
  - Clear search history with one click

**Filtering Options:**
- Filter by recipe category/tags
- Filter by difficulty level
- **Reset Filters:** Quickly reset all filters to default values

**Sorting Options:**
- Sort by newest recipes
- Sort by most liked recipes (Most Popular - default)
- Sort by difficulty level

**Smart Features:**
- Filters persist when changing search keywords
- URL-based state persistence for shareable search results

#### 4. **View Reviews & Ratings**
- **View ratings:** See average ratings and other user reviews
- **View community feedback:** Read detailed reviews from other users
- Browse recipe feedback to inform your cooking decisions

**Note:** Guests cannot write reviews, rate recipes, like recipes, create recipes, save favorites, or edit their profile until their account is approved by an admin and status changes from "Pending" to "Active"

---

<a id="installation-setup"></a>
##  Installation & Setup

### Prerequisites
- **Node.js** v16 or higher
- **npm** (comes with Node.js)

### Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd recipe-sharing-system
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Start Development Server**
   ```bash
   npm run dev
   ```
   The application will open at `http://localhost:5173`

4. **Build for Production**
   ```bash
   npm run build
   ```

5. **Preview Production Build**
   ```bash
   npm run preview
   ```

<a id="available-scripts"></a>
## 📦 Available Scripts

| Script | Purpose |
|--------|---------|
| `npm run dev` | Start development server with hot reload |
| `npm run build` | Build optimized production bundle |
| `npm run preview` | Preview the production build locally |
| `npm run lint` | Run ESLint to check code quality |

<a id="project-structure"></a>
## 📁 Project Structure

```
recipe-sharing-system/
├── .serena/                   # Project memories used for development (memory bank)
├── guides/                    # Documentation and setup guides
│   ├── database_implementation_logic_explanation.md
│   └── SETUP_GUIDE_PHPMYADMIN.md
├── lucid_diagrams/            # Lucidchart-exported diagrams (PNG/SVG)
├── mermaid-diagrams/          # Mermaid diagram files (.mmd)
│   ├── application_flowchart.mmd
│   └── data-flow-from-py.mmd
├── plan/                      # Future development planning documents
│   └── upgrade-database-integration-1.md
├── python_diagrams/           # Graphviz Python diagram generators
│   ├── data_flow_graphviz.py
│   ├── er_recipe_conceptual_graphviz.py
│   ├── er_recipe_logical_graphviz.py
│   ├── flowchart_graphviz.py
│   └── out/                   # Generated diagram images
├── public/                    # Static assets
├── src/
│   ├── components/           # Reusable UI components
│   │   ├── layout/          # Navigation & layout components
│   │   │   ├── Navbar.jsx
│   │   │   └── Sidebar.jsx
│   │   ├── recipe/          # Recipe-specific components
│   │   │   └── RecipeCard.jsx
│   │   └── ui/              # Generic UI components
│   │       ├── Badge.jsx
│   │       ├── Button.jsx
│   │       ├── Card.jsx
│   │       ├── Input.jsx
│   │       ├── Modal.jsx
│   │       ├── Table.jsx
│   │       └── Tabs.jsx
│   ├── context/             # React context for state management
│   │   └── AuthContext.jsx  # Authentication, user state & session tracking
│   ├── layouts/             # Layout templates for different routes
│   │   ├── AdminLayout.jsx
│   │   ├── AuthLayout.jsx
│   │   └── RootLayout.jsx
│   ├── lib/                 # Utilities & helpers
│   │   ├── storage.js       # LocalStorage management, seed data & activity logging
│   │   └── utils.js         # Helper functions
│   ├── pages/               # Page components
│   │   ├── Auth/            # Authentication pages
│   │   │   ├── Login.jsx
│   │   │   └── Signup.jsx
│   │   ├── Admin/           # Admin pages
│   │   │   ├── AdminRecipes.jsx
│   │   │   ├── AdminStats.jsx
│   │   │   └── UserList.jsx
│   │   └── Recipe/          # Recipe & user pages
│   │       ├── CreateRecipe.jsx
│   │       ├── Home.jsx
│   │       ├── Profile.jsx
│   │       ├── RecipeDetail.jsx
│   │       └── Search.jsx
│   ├── App.jsx              # Main application component
│   ├── main.jsx             # Application entry point
│   └── index.css            # Global styles
├── public/                  # Static assets
├── package.json             # Project dependencies & scripts
├── vite.config.js          # Vite configuration
├── eslint.config.js        # ESLint configuration
└── README.md               # This file
```

<a id="technologies-used"></a>
## 🛠️ Technologies Used

### Frontend Framework
- **React** (v19.2.0) - Modern UI library
- **React Router DOM** (v7.12.0) - Client-side routing
- **React DOM** (v19.2.0) - React rendering engine

### Styling & UI
- **Tailwind CSS** (v4.1.18) - Utility-first CSS framework
- **Tailwind CSS Vite Plugin** (v4.1.18) - Build tool integration
- **Tailwind Merge** (v3.4.0) - Intelligent class merging
- **Lucide React** (v0.562.0) - Icon library

### Build & Development
- **Vite** (v7.2.4) - Fast build tool
- **Vite React Plugin** (v5.1.1) - React optimization for Vite
- **ESLint** (v9.39.1) - Code quality tool

### Utilities
- **Clsx** (v2.1.1) - Conditional className utility
- **date-fns** (v4.1.0) - Modern JavaScript date utility library for formatting and manipulation

<a id="system-diagrams"></a>
## 📊 System Diagrams

The project includes comprehensive visual documentation to help understand the system architecture, data flows, and relationships. These diagrams are available in two formats:

### Diagram Types

#### 1. **Application Flowchart**
Illustrates the complete user journey and application workflow, including authentication, role-based access, and feature interactions.

- **Location:** 
  - Mermaid: [mermaid-diagrams/application_flowchart_clean.mmd](mermaid-diagrams/application_flowchart_clean.mmd)
  - Graphviz: [python_diagrams/flowchart_graphviz.py](python_diagrams/flowchart_graphviz.py)
- **Shows:** User flows, decision points, authentication paths, admin workflows, contributor features, and guest limitations

#### 2. **Data Flow Diagram (DFD)**
Depicts how data moves through the system between users, processes, and storage.

- **Location:** 
  - Mermaid: [mermaid-diagrams/data-flow-from-py.mmd](mermaid-diagrams/data-flow-from-py.mmd)
  - Graphviz: [python_diagrams/data_flow_graphviz.py](python_diagrams/data_flow_graphviz.py)
- **Shows:** Data inputs/outputs, processing flows, localStorage interactions, authentication data flows, and recipe management pipelines

#### 3. **Entity-Relationship Diagrams (ERD)**
Visualizes the data model with entities, attributes, and relationships used in localStorage.

##### Conceptual ERD
- **Location:** [python_diagrams/er_recipe_conceptual_graphviz.py](python_diagrams/er_recipe_conceptual_graphviz.py)
- **Shows:** High-level entities (User, Recipe, Review, etc.) and their relationships without implementation details

##### Logical ERD
- **Location:** [python_diagrams/er_recipe_logical_graphviz.py](python_diagrams/er_recipe_logical_graphviz.py)
- **Shows:** Detailed data structure including all attributes, primary keys, foreign keys, and cardinalities

### How to Generate/View Diagrams

**Mermaid Diagrams (.mmd files):**
- Open in VS Code with Mermaid extension installed
- Preview using the Mermaid preview feature
- Render online at [mermaid.live](https://mermaid.live)

**Graphviz Python Diagrams:**
1. Install Graphviz: 
   ```bash
   pip install graphviz
   ```
2. Run the Python script:
   ```bash
   python python_diagrams/<diagram_name>.py
   ```
3. Generated images are saved in `python_diagrams/out/` directory

These diagrams provide comprehensive documentation for understanding the system's architecture, data structures, and user workflows.

#### Lucid Diagrams

- **Location:** `lucid_diagrams/` — contains exported diagram images (PNG or SVG) created in Lucidchart for quick visual reference and presentation.

<a id="data-storage"></a>
## 💾 Data Storage

The application uses **browser localStorage** for data persistence:

### Stored Data
1. **User Accounts** - All registered user profiles and credentials
2. **Recipes** - All submitted recipes with their metadata
3. **Reviews & Ratings** - User feedback on recipes (enforces one per user per recipe)
4. **Session Data** - Current logged-in user information
5. **Search History** - User search queries with timestamps (query-only, no filters)
6. **Daily Stats** - Page views, active users per day
7. **Activity Logs** - Admin action history (user management, recipe approvals)

### Initial Data
The application comes with **comprehensive seed data** including:

**User Accounts:**
- 3 Admin accounts with different activity levels
- 7 User accounts spanning all statuses (Active, Inactive, Pending)
- Mix of Contributors and regular Users
- Pre-configured profiles with avatars, bios, and cooking levels

**Recipe Content:**
- 10+ diverse recipes across multiple categories (Breakfast, Lunch, Dinner, Dessert, Snack)
- Varying difficulty levels (Easy, Medium, Hard)
- Different approval statuses (Published, Pending, Rejected) for testing workflows
- Complete recipe data including ingredients, instructions, prep/cook times, servings
- Recipe metadata: views, likes, favorites

**Engagement Data:**
- Pre-filled reviews and ratings from multiple users
- Sample favorites/bookmarks for user accounts
- View counts and like counts on recipes
- Historical daily stats for analytics dashboard

**Admin Data:**
- Recent activity log entries showing user management and recipe approvals
- Daily statistics for testing dashboard metrics
- Sample data spanning multiple days for trend analysis

This rich seed data allows you to immediately explore all features without creating accounts or recipes from scratch.

### Test Credentials

**Admin Accounts:**
| Email | Password | Name |
|-------|----------|------|
| `admin@cookhub.com` | `admin` | Admin User |
| `olivia@cookhub.com` | `admin` | Olivia Admin |
| `marcus@cookhub.com` | `admin` | Marcus Admin |

**Sample User Accounts:**
| Email | Password | Name | Role | Status |
|-------|----------|------|------|--------|
| `user@cookhub.com` | `user` | John Doe | User | Active/Inactive |
| `maria@cookhub.com` | `maria123` | Maria Garcia | User | Active/Inactive |
| `tom@cookhub.com` | `tom123` | Tom Baker | User | Suspended |
| `amy@cookhub.com` | `amy123` | Amy Wilson | User | Pending |
| `kevin@cookhub.com` | `kevin123` | Kevin Tran | User | Pending |
| `sarah@cookhub.com` | `sarah123` | Sarah Kim | User | Active/Inactive |
| `daniel@cookhub.com` | `daniel123` | Daniel Rivera | User | Active/Inactive |
| `lina@cookhub.com` | `lina123` | Lina Patel | User | Active/Inactive |
| `omar@cookhub.com` | `omar123` | Omar Hassan | User | Pending |

### Resetting Data

To reset all data to the initial seed state, open the browser console and run:
```javascript
localStorage.clear();
location.reload();
```
Or use the storage utility:
```javascript
import { storage } from './src/lib/storage';
storage.resetData();
```
Or manually delete in the browser console -> Application -> Local storage

<a id="support"></a>
## 📧 Support

For issues, questions, or contributions, please contact the development team or submit an issue through the project repository.
