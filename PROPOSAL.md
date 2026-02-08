# Kitchen Odyssey: A Collaborative Recipe Sharing, Management & Discovery Platform

## 1. Project Title
**Kitchen Odyssey: A Collaborative Recipe Sharing, Management & Discovery Platform**

## 2. Project Overview
Kitchen Odyssey is a community recipe sharing platform where people can discover recipes and (when approved) contribute recipes. The system includes role-based access and moderation workflows to maintain content quality.

## 3. Goals & Objectives
-	Provide a clean User Experience for browsing and searching recipes.
-	Support contributors in creating and managing recipes.
-	Enforce admin moderation for both users and recipes.
-	Track platform engagement (DAU, views, activity logs).

## 4. Project Type
-	Web Application
-	POC for Senior Project: Yes

## 5. Team Members
-	Member 1: Aung Thura Hein (6726135)
-	Member 2: Sithu Win San (6726077)

## 6. Problem Statement
Many recipe platforms support discovery but provide limited moderation and onboarding for contributors. This project addresses:
-	Moderated recipe publication (approval before public listing)
-	Account approval lifecycle (pending → active) and restricted interactions for pending/suspended users
-	Discovery + engagement features (search, likes, favorites, ratings/reviews)
-	Admin analytics and activity auditing

**Target Users:**
- **Home cooks** who want to discover and try new recipes
- **Food enthusiasts** who want to share their culinary creations
- **Professional chefs** who want to showcase their expertise
- **Community administrators** who need tools to manage users and moderate content

**Why this matters:**
A centralized recipe-sharing platform promotes culinary creativity, preserves family and cultural recipes, and creates a supportive community for food lovers. With growing interest in home cooking, there's a need for an accessible, user-friendly platform that balances ease of use with content quality control through approval workflows.

## 7. Roles & Features

### 7.1 Roles
-	**Admin**
-	**Contributor** (Activated User)
-	**Guest** (No Sign-in)

### 7.2 Features

#### 7.2.1 Admin Features
-	User management: view users, update status (activate/deactivate/suspend), delete accounts
-	Recipe management: approve/reject/delete recipes
-	Analytics dashboard: daily active users (DAU), daily views, pending vs published recipe counts
-	Activity feed: logs admin actions (user status changes, recipe approvals/rejections/deletions)

#### 7.2.2 Contributor Features
-	Recipe creation and editing (owner-only)
-	Recipe submission workflow (pending → published/rejected)
-	Engagement: likes and favorites
-	Reviews: rating + comment (one review per user per recipe)
-	Search: keyword search + personal search history (deduped and limited)

#### 7.2.3 Guest Features
-	Browse published recipes
-	Search published recipes
-	View recipe detail pages and read reviews/ratings

### 7.3 Status Gating
-	Pending or Suspended users: can authenticate but are blocked from interaction features until activated from Admin. (Same features as Guest)

## 8. Workflows

### 8.1 Account Approval
1.	User signs up → status = pending
2.	Admin activates account → status = active
3.	User gains interaction privileges (likes, favorites, reviews, recipe submissions)

### 8.2 Recipe Approval
1.	Contributor submits recipe → status = pending
2.	Admin reviews recipe → published (approved) or rejected
3.	Only published recipes are visible to non-admin viewers

### 8.3 Engagement & Tracking
-	Recipe views are recorded once per viewer (contributor-only key)
-	Daily stats record DAU and daily views

## 9. Proposed CRUD

### 9.1 Guest (CRUD)
In Guest mode, user skips login/signup.
-	GET recipes
-	POST search for a recipe
-	GET recipe details
-	GET reviews

### 9.2 Auth (CRUD)
-	POST signup
-	POST login
-	POST logout
-	GET current user info

### 9.3 Admin (CRUD)
-	GET all users
-	POST users (admin-create, optional)
-	GET user
-	PUT user (self update; admin update)
-	DELETE user
-	PATCH update user status { status: "active" | "inactive" | "pending" | "suspended" }

### 9.4 Recipes (CRUD)
-	GET recipes (published only for guests/normal users)
-	POST recipes (active users; creates pending)
-	GET recipe
-	PUT recipe (owner; rejected recipes can resubmit → pending)
-	DELETE recipe (owner or admin)
-	PATCH update recipe status (admin) body: { status: "published" | "rejected" }
-	POST like
-	POST favorite
-	POST view

### 9.5 Reviews (CRUD)
-	GET reviews
-	POST reviews
-	PUT review
-	DELETE review

### 9.6 Search History (CRUD)
-	GET current search history
-	POST add query
-	DELETE clear current search history

### 9.7 Analytics & Activity (Admin)
-	GET daily stats
-	GET activity

## 10. Project Scope & Features

**Core Features**

**User Management & Authentication**
- User registration with role-based access control (Admin, Contributor, Guest/Pending)
- Secure login/logout functionality
- User profile management (bio, avatar, cooking level, location)
- User status system (Pending → Active after admin approval)
- User activity tracking (last active timestamp, DAU metrics)
- Account suspension by administrators

**Recipe Management**
- Create new recipes with detailed information (title, description, ingredients, instructions)
- Upload or link recipe images
- Edit existing recipes (by recipe author)
- Delete recipes (by author or admin)
- Recipe submission workflow (Pending → Published after admin approval)
- Dynamic ingredient sections with quantity and units
- Recipe categorization (Breakfast, Lunch, Dinner, Dessert, etc.)
- Difficulty levels (Easy, Medium, Hard)
- Preparation time and cooking time tracking
- Serving size specifications

**Recipe Discovery & Interaction**
- Browsing published recipes in a grid/card layout
- Advanced search functionality with keyword matching
- Filter by category and difficulty
- Sort by newest, most viewed, or most liked
- View detailed recipe information
- Interactive ingredient checklist (mark off while cooking)
- View recipe statistics (preparation time, cooking time, servings, difficulty)

**User Engagement**
- Like/unlike recipes (one like per user per recipe)
- Favorite/unfavorite recipes (personal recipe collection)
- Rate recipes (1-5 stars) with written reviews
- One review limit per user per recipe to prevent spam
- View author information and other recipes by same author
- View recipe view counts and like counts

**Admin Dashboard & Controls**
- View real-time site analytics and metrics
- Total users, published recipes, pending recipes statistics
- Daily active users (DAU) tracking with session heartbeat
- Daily view counts and engagement metrics
- User management with status changes (activate/suspend)
- View detailed user list with filtering
- Recipe approval workflow (approve/reject pending recipes)
- Content moderation and deletion
- Recent activity feed tracking admin actions
- View and manage all system content

**Search & Navigation**
- Responsive navigation with sidebar
- Quick search bar on homepage
- Search results page with filters
- Browse by category functionality
- Personal recipe collection (My Recipes tab)
- Random recipe discovery feature

## 11. Data Models

**Entity 1: User**
- **Fields**:
  - id (auto-generated ObjectId)
  - username (string, unique, required)
  - firstName (string, required)
  - lastName (string, required)
  - email (string, unique, required, indexed)
  - password (hashed string, required)
  - birthday (date)
  - role (enum: 'admin' | 'user')
  - status (enum: 'active' | 'pending' | 'suspended', default: 'pending')
  - joinedDate (datetime, default: current timestamp)
  - lastActive (datetime, updated on logout/browser close)
  - avatar (string, URL)
  - bio (text)
  - location (string)
  - cookingLevel (enum: 'Beginner' | 'Intermediate' | 'Advanced' | 'Professional')
  - favorites (array of recipe IDs)
  - viewedRecipes (array of viewed recipe records)
  - searchHistory (array of search query records)
- **Operations**: Create (User registration), Read (View profile, list users), Update (Update profile by user, admin can change status/role), Delete (Admin can delete user accounts)

**Entity 2: Recipe**
- **Fields**:
  - id (auto-generated ObjectId)
  - title (string, required, indexed for search)
  - description (text, required)
  - categories (array of strings, required)
  - ingredients (array of objects with name, quantity, unit)
  - instructions (array of strings, required)
  - prepTime (number, in minutes)
  - cookTime (number, in minutes)
  - servings (number, default: 2)
  - difficulty (enum: 'Easy' | 'Medium' | 'Hard')
  - image (string, URL)
  - authorId (ObjectId reference to User, indexed)
  - status (enum: 'published' | 'pending', default: 'pending')
  - createdAt (datetime, default: current timestamp)
  - views (number, default: 0)
  - likes (array of user IDs who liked this recipe)
- **Operations**: Create (Contributor submits recipe, status: pending), Read (View recipe details, list recipes with filters), Update (Edit by recipe author), Delete (By author or admin), Update Status (Admin approves/rejects pending recipes)

**Entity 3: Review**
- **Fields**:
  - id (auto-generated ObjectId)
  - recipeId (ObjectId reference to Recipe, indexed)
  - userId (ObjectId reference to User, indexed)
  - rating (number, 1-5, required)
  - comment (text, required)
  - createdAt (datetime, default: current timestamp)
- **Operations**: Create (Submit review, one per user per recipe enforced), Read (Fetch reviews for a recipe), Delete (By review author)

**Entity 4: ActivityLog** (Admin Tracking)
- **Fields**:
  - id (auto-generated ObjectId)
  - adminId (ObjectId reference to User, required)
  - action (enum: 'user_status_change' | 'recipe_approval' | 'recipe_rejection' | 'recipe_deletion' | 'user_deletion')
  - entityType (enum: 'user' | 'recipe')
  - entityId (ObjectId reference)
  - actionDetails (text)
  - createdAt (datetime, default: current timestamp)
- **Operations**: Create (Automatic logging of admin actions), Read (Fetch activity logs)

**Entity 5: DailyStats** (Analytics)
- **Fields**:
  - id (auto-generated ObjectId)
  - date (date, unique, required, indexed)
  - dailyActiveUsers (number, default: 0)
  - dailyViews (number, default: 0)
  - publishedRecipes (number, default: existing count)
  - pendingRecipes (number, default: existing count)
  - totalUsers (number, default: existing count)
- **Operations**: Create (New daily entry), Update (Incremental updates throughout day), Read (Fetch analytics for dashboard)

## 12. Technology Stack

**Frontend:**
- ReactJS 19.2 (UI library with modern hooks and concurrent features)
- React Router DOM 7.13 (Client-side routing)
- Vite 7.2 (Build tool for fast development and optimized production builds)
- Tailwind CSS 4.1 (Utility-first CSS framework for rapid styling)
- Lucide React 0.56 (Icon library)

**Backend:**
- Next.js 15 (App Router) (React framework for full-stack development)
- Next.js API Routes (RESTful API endpoints)
- Next.js Middleware (Authentication and route protection)

**Database:**
- MongoDB Atlas (Cloud-hosted NoSQL database)
- Mongoose ODM (Object Data Modeling for MongoDB)
- MongoDB Aggregation Framework (Complex queries for analytics)

**Deployment:**
- Azure Static Web Apps (Frontend deployment)
- Azure App Service (Backend API deployment)
- Azure Storage (Image/file storage for recipe images)
- Azure Key Vault (Secret management for database credentials and API keys)
- Azure Application Insights (Monitoring and analytics)

## 13. Expected Outcomes
The completed CookHub platform is aimed at delivering a moderated, user-friendly recipe sharing site that enhances discovery and contribution while ensuring content quality. Key outcomes include high user retention via engagement tools, efficient admin oversight, and scalable analytics for monitoring.
