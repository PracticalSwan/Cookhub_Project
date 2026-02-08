# Kitchen Odyssey: A Collaborative Recipe Sharing, Management & Discovery Platform

## 1. Project Title
**Kitchen Odyssey: A Collaborative Recipe Sharing, Management & Discovery Platform**

**Project Type**
- Web Application
- POC for Senior Project: Yes

## 2. Team Members
- Member 1: Aung Thura Hein (6726135)
- Member 2: Sithu Win San (6726077)

## 3. Problem Statement & Motivation

**What problem does this system solve?**

Many existing recipe platforms support discovery but provide limited moderation and onboarding for contributors. Kitchen Odyssey addresses these gaps by implementing:
- Moderated recipe publication with approval workflow (pending → published/rejected)
- Account approval lifecycle (pending → active) to ensure quality contributors
- Restricted interactions for pending/suspended users to maintain community standards
- Comprehensive discovery and engagement features (search, likes, favorites, ratings/reviews)
- Admin analytics and activity auditing for platform oversight

**Who is the target user?**

- **Home cooks** who want to discover and try new recipes
- **Food enthusiasts** who want to share their culinary creations with a community
- **Professional chefs** who want to showcase their expertise and build a following
- **Community administrators** who need robust tools to manage users and moderate content

**Why does this problem matter?**

A centralized recipe-sharing platform promotes culinary creativity, preserves family and cultural recipes, and creates a supportive community for food lovers. With growing interest in home cooking and DIY food preparation, there's an increasing need for an accessible, user-friendly platform that balances ease of use with content quality control. By implementing approval workflows for both users and recipes, Kitchen Odyssey ensures high-quality content while preventing spam and maintaining community standards. The platform also provides analytics and engagement tracking to help administrators understand and improve the community experience.

## 4. Project Scope & Features

### Core Features

**User Management & Authentication**
- User registration with role-based access control (Admin, Contributor, Guest/Pending)
- Secure login/logout functionality with session management
- User profile management (bio, avatar, cooking level, location)
- User status system (Pending → Active after admin approval)
- User activity tracking (last active timestamp, DAU metrics)
- Account suspension by administrators
- Status gating: Pending or Suspended users can authenticate but are blocked from interaction features until activated (same access as Guest users)

**Recipe Management**
- Create new recipes with detailed information (title, description, ingredients, instructions)
- Upload or link recipe images
- Edit existing recipes (by recipe author only)
- Delete recipes (by author or admin)
- Recipe submission workflow (Pending → Published after admin approval or Rejected)
- Dynamic ingredient sections with quantity and units
- Recipe categorization (Breakfast, Lunch, Dinner, Dessert, etc.)
- Difficulty levels (Easy, Medium, Hard)
- Preparation time and cooking time tracking
- Serving size specifications
- Only published recipes are visible to non-admin viewers

**Recipe Discovery & Interaction**
- Browsing published recipes in a grid/card layout
- Advanced search functionality with keyword matching
- Filter by category and difficulty
- Sort by newest, most viewed, or most liked
- View detailed recipe information
- Interactive ingredient checklist (mark off while cooking)
- View recipe statistics (preparation time, cooking time, servings, difficulty)
- Guest access: Browse published recipes, search recipes, view recipe details and reviews (no authentication required)

**User Engagement**
- Like/unlike recipes (one like per user per recipe)
- Favorite/unfavorite recipes (personal recipe collection)
- Rate recipes (1-5 stars) with written reviews
- One review limit per user per recipe to prevent spam
- View author information and other recipes by same author
- View recipe view counts and like counts
- Recipe views recorded once per viewer (contributor-only key)

**Admin Dashboard & Controls**
- View real-time site analytics and metrics
- Total users, published recipes, pending recipes statistics
- Daily active users (DAU) tracking with session heartbeat
- Daily view counts and engagement metrics
- User management: view users, update status (activate/deactivate/suspend), delete accounts
- View detailed user list with filtering
- Recipe management: approve/reject/delete recipes
- Recipe approval workflow (approve/reject pending recipes)
- Content moderation and deletion
- Recent activity feed: logs admin actions (user status changes, recipe approvals/rejections/deletions)
- Activity tracking for audit trails
- View and manage all system content

**Search & Navigation**
- Responsive navigation with header
- Quick search bar on homepage
- Search results page with filters
- Browse by category functionality
- Personal recipe collection (My Recipes tab)
- Personal search history (deduplicated and limited)
- Random recipe discovery feature

### Workflows

**Account Approval Workflow**
1. User signs up → status = pending
2. Admin activates account → status = active
3. User gains interaction privileges (likes, favorites, reviews, recipe submissions)

**Recipe Approval Workflow**
1. Contributor submits recipe → status = pending
2. Admin reviews recipe → published (approved) or rejected
3. Only published recipes are visible to non-admin viewers
4. Rejected recipes can be edited and resubmitted → status reverts to pending

**Engagement & Tracking**
- Recipe views are recorded once per viewer (contributor-only key)
- Daily stats record DAU and daily views
- Activity logs track all admin actions for audit purposes

### User Roles & Permissions

**Admin**
- Full access to all features
- User management capabilities
- Recipe moderation and approval
- Analytics dashboard access
- Activity log viewing

**Contributor (Activated User)**
- Create and edit own recipes
- Submit recipes for approval
- Like and favorite recipes
- Write reviews and ratings
- Access search history
- View profile and statistics

**Guest (No Sign-in / Pending Users)**
- Browse published recipes
- Search published recipes
- View recipe detail pages and read reviews/ratings
- No interaction privileges (no likes, favorites, or reviews)

## 5. Data Models

The system uses 5 entities to support comprehensive recipe sharing, user management, and platform analytics. All entities support full CRUD operations with role-based access control.

### Entity 1: User
**Fields:**
- id (auto-generated ObjectId, primary key)
- username (string, unique, required, indexed)
- firstName (string, required)
- lastName (string, required)
- email (string, unique, required, indexed)
- password (hashed string, required)
- birthday (date)
- role (enum: 'admin' | 'user', default: 'user')
- status (enum: 'active' | 'pending' | 'suspended', default: 'pending')
- joinedDate (datetime, default: current timestamp)
- lastActive (datetime, updated on logout/browser close)
- avatar (string, URL)
- bio (text, optional)
- location (string, optional)
- cookingLevel (enum: 'Beginner' | 'Intermediate' | 'Advanced' | 'Professional')
- favorites (array of recipe ObjectIds)
- viewedRecipes (array of viewed recipe records with recipeId and timestamp)
- searchHistory (array of search query records with query text and timestamp)

**Operations:**
- **Create**: User registration (POST /api/auth/signup)
- **Read**: View own profile (GET /api/users/me), View user by ID (GET /api/users/:id), List all users (GET /api/users - admin only)
- **Update**: Update own profile (PUT /api/users/me), Admin can update user status (PATCH /api/users/:id/status)
- **Delete**: Admin can delete user accounts (DELETE /api/users/:id)

### Entity 2: Recipe
**Fields:**
- id (auto-generated ObjectId, primary key)
- title (string, required, indexed for search)
- description (text, required)
- categories (array of strings, required, e.g., ['Breakfast', 'Quick Meals'])
- ingredients (array of objects with name, quantity, unit)
- instructions (array of strings, required, step-by-step)
- prepTime (number, in minutes)
- cookTime (number, in minutes)
- servings (number, default: 2)
- difficulty (enum: 'Easy' | 'Medium' | 'Hard')
- image (string, URL)
- authorId (ObjectId reference to User, indexed)
- status (enum: 'published' | 'pending' | 'rejected', default: 'pending')
- createdAt (datetime, default: current timestamp)
- updatedAt (datetime, auto-updated on modification)
- views (number, default: 0)
- likes (array of user ObjectIds who liked this recipe)

**Operations:**
- **Create**: Contributor submits recipe with status 'pending' (POST /api/recipes)
- **Read**: View recipe details (GET /api/recipes/:id), List recipes with filters (GET /api/recipes - published only for non-admin), Search recipes (POST /api/recipes/search)
- **Update**: Edit by recipe author (PUT /api/recipes/:id), Admin approves/rejects (PATCH /api/recipes/:id/status), Record view (POST /api/recipes/:id/view), Like/Unlike recipe (POST /api/recipes/:id/like), Favorite/Unfavorite (POST /api/recipes/:id/favorite)
- **Delete**: By recipe author or admin (DELETE /api/recipes/:id)

### Entity 3: Review
**Fields:**
- id (auto-generated ObjectId, primary key)
- recipeId (ObjectId reference to Recipe, indexed)
- userId (ObjectId reference to User, indexed)
- rating (number, 1-5, required)
- comment (text, required)
- createdAt (datetime, default: current timestamp)
- updatedAt (datetime, auto-updated on modification)

**Constraints:**
- Unique constraint on (recipeId, userId) combination to enforce one review per user per recipe

**Operations:**
- **Create**: Submit review (POST /api/reviews) - enforces one review per user per recipe
- **Read**: Fetch reviews for a recipe (GET /api/reviews?recipeId=:id), Fetch user's reviews (GET /api/reviews?userId=:id)
- **Update**: Edit own review (PUT /api/reviews/:id)
- **Delete**: Delete own review (DELETE /api/reviews/:id)

### Entity 4: ActivityLog
**Fields:**
- id (auto-generated ObjectId, primary key)
- adminId (ObjectId reference to User, required)
- action (enum: 'user_status_change' | 'recipe_approval' | 'recipe_rejection' | 'recipe_deletion' | 'user_deletion', required)
- entityType (enum: 'user' | 'recipe', required)
- entityId (ObjectId reference to User or Recipe)
- actionDetails (text, description of the action taken)
- createdAt (datetime, default: current timestamp, indexed)

**Operations:**
- **Create**: Automatic logging of admin actions (POST /api/activity - system internal)
- **Read**: Fetch activity logs (GET /api/activity - admin only), Filter by date range, action type, or entity
- **Update**: Not applicable (immutable audit log)
- **Delete**: Not applicable (permanent audit trail)

### Entity 5: DailyStats
**Fields:**
- id (auto-generated ObjectId, primary key)
- date (date, unique, required, indexed)
- dailyActiveUsers (number, default: 0, count of unique users with lastActive on this date)
- dailyViews (number, default: 0, total recipe views on this date)
- publishedRecipes (number, default: 0, total published recipes as of this date)
- pendingRecipes (number, default: 0, total pending recipes as of this date)
- totalUsers (number, default: 0, total registered users as of this date)
- createdAt (datetime, default: current timestamp)
- updatedAt (datetime, auto-updated on modification)

**Operations:**
- **Create**: New daily entry created automatically (POST /api/stats - system internal)
- **Read**: Fetch analytics for dashboard (GET /api/stats), Filter by date range
- **Update**: Incremental updates throughout the day (PATCH /api/stats/:date - system internal)
- **Delete**: Not applicable (historical data preservation)

### CRUD Summary

All entities support standard CRUD operations with appropriate access control:
- **Users**: Full CRUD with role-based restrictions (admin vs. self-edit)
- **Recipes**: Full CRUD with status workflow (pending/published/rejected) and ownership validation
- **Reviews**: Full CRUD with one-review-per-user constraint and ownership validation
- **ActivityLog**: Create and Read only (immutable audit trail)
- **DailyStats**: Create, Read, and Update (no Delete for historical preservation)

## 6. Technology Stack

**Frontend:**
- ReactJS 19.2 - UI library with modern hooks and concurrent features
- React Router DOM 7.13 - Client-side routing and navigation
- Vite 7.2 - Build tool for fast development and optimized production builds
- Tailwind CSS 4.1 - Utility-first CSS framework for rapid styling and responsive design
- Lucide React 0.56 - Modern icon library for UI elements

**Backend:**
- Next.js 15 (App Router) - React framework for full-stack development with server-side rendering
- Next.js API Routes - RESTful API endpoints for backend logic
- Next.js Middleware - Authentication and route protection
- bcrypt - Password hashing and security
- JWT (JSON Web Tokens) - Secure authentication tokens

**Database:**
- MongoDB Atlas - Cloud-hosted NoSQL database for scalable data storage
- Mongoose ODM (Object Data Modeling) - Schema-based solution for MongoDB data modeling
- MongoDB Aggregation Framework - Complex queries for analytics and reporting

**Deployment:**
- Azure Static Web Apps - Frontend deployment with global CDN
- Azure App Service - Backend API deployment with auto-scaling
- Azure Storage - Image/file storage for recipe images and user avatars
- Azure Key Vault - Secret management for database credentials and API keys
- Azure Application Insights - Monitoring, analytics, and performance tracking

**Development Tools:**
- ESLint - Code linting and quality enforcement
- Git & GitHub - Version control and collaboration
- pnpm - Fast, disk space efficient package manager
