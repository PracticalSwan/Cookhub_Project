# Kitchen Odyssey: A Collaborative Recipe Sharing, Management & Discovery Platform

## 1. Project Title
Kitchen Odyssey: A Collaborative Recipe Sharing, Management & Discovery Platform

Project Type
• Web Application
• POC for Senior Project: Yes

## 2. Team Members
• Member 1: Aung Thura Hein (6726135)
• Member 2: Sithu Win San (6726077)

## 3. Problem Statement & Motivation

### 3.1 What problem does this system solve?
Many recipe platforms support discovery but provide limited moderation and onboarding for contributors. This project addresses:
• Moderated recipe publication with approval workflow (pending to published/rejected)
• Account approval lifecycle to ensure quality contributors (pending to activated)
• Restricted interactions for pending/suspended users to maintain community standards
• Comprehensive discovery and engagement features (search, likes, favorites, ratings/reviews)
• Admin analytics and activity auditing for platform oversight

### 3.2 Who are the target users?
• Independent individuals cooking out of necessity
• Home cooks who want to discover and try new and reliable recipes
• Food enthusiasts who want to share their culinary creations with community
• Chefs who want to showcase their expertise
• Community administrators who need robust tools to manage users and moderate content

### 3.3 Why does this problem matter?
A recipe-sharing platform like Kitchen Odyssey encourages creativity, preserves family and cultural recipes, and builds a welcoming community for food lovers. With more people cooking at home, there's a need for an easy-to-use website that keeps content reliable. By requiring approval for new users and recipes, Kitchen Odyssey stays trustworthy, blocks spams, and maintains good standard. The built-in analytics tool also helps admins track engagement and improve community experiences.

## 4. Project Scope & Features

### 4.1 Core Features

#### 4.1.1 User Management & Authentication
• User registration with role-based access control (Admin, Contributor, Guest/Pending)
• Secure login/logout functionality with session management
• User profile management (bio, avatar, cooking level, location)
• User status system (pending → activated after admin approval)
• User activity tracking (last active timestamp, DAU metrics)
• Account suspension by administrators
• Status gating: Pending or Suspended users can authenticate but are blocked from interaction features until activated (same access as Guest users)

#### 4.1.2 Recipe Management
• Create new recipes with detailed information (title, description, ingredients, instructions)
• Upload or link recipe images
• Edit existing recipes (by recipe author only)
• Delete recipes (by author or admin)
• Recipe submission workflow (pending → published after admin approval or rejected)
• Dynamic ingredient sections with quantity and units
• Recipe categorization (breakfast, lunch, dinner, dessert, etc.)
• Difficulty levels (Easy, Medium, Hard)
• Preparation time and cooking time tracking
• Serving size specifications
• Only published recipes are visible to non-admin viewers

#### 4.1.3 Recipe Discovery & Interaction
• Browsing published recipes in a grid/card layout
• Advanced search functionality with keyword matching
• Filter by category and difficulty
• Sort by newest, most viewed, or most liked
• View detailed recipe information
• Interactive ingredient checklist (mark off while cooking)
• Guest access: Browse published recipes, search recipes, view recipe details and reviews (no authentication required)

#### 4.1.4 User Engagement
• Like/unlike recipes (one like per user per recipe)
• Favorite/unfavorite recipes (personal recipe collection)
• Rate recipes (1-5 stars) with written reviews
• One review limit per user per recipe to prevent spam
• View author information and other recipes by same author
• View recipe view counts and like counts
• Recipe views recorded once per viewer (contributor-only key)

#### 4.1.5 Admin Dashboard & Controls
• View real-time site analytics and metrics
• Total users, published recipes, pending recipes statistics
• Daily active users (DAU) tracking with session heartbeat
• Daily view counts and engagement metrics
• User management: view users, update status (activate/deactivate/suspend), delete accounts
• View detailed user list with filtering
• Recipe management: approve/reject/delete recipes
• Recipe approval workflow (approve/reject pending recipes)
• Content moderation and deletion
• Recent activity feed: logs admin actions (user status changes, recipe approvals/rejections/deletions)
• Activity tracking for audit trails
• View and manage all system content

#### 4.1.6 Search & Navigation
• Responsive navigation with header
• Quick search bar on homepage
• Search results page with filters
• Browse by category functionality
• Personal recipe collection
• Personal search history
• Random recipe discovery feature

### 4.2 Workflows

#### 4.2.1 Account Approval Workflow
1. User signs up → status: pending
2. Admin activates account → status: activated
3. User gains interaction privileges (likes, favorites, reviews, recipe submissions)

#### 4.2.2 Recipe Approval
1. Contributor submits recipe → status: pending
2. Admin reviews recipe → published (approved) or rejected
3. Only published recipes are visible to non-admin viewers
4. Rejected recipes can be edited and resubmitted → status reverts to pending

#### 4.2.3 Engagement & Tracking
• Recipe views are recorded once per viewer (contributor-only key)
• Daily stats record DAU and daily views
• Activity logs track all admin actions for audit purposes

### 4.3 User Roles & Permissions

#### 4.3.1 Admin
• User management capabilities
• Recipe moderation and approval
• Analytics dashboard access
• Activity log viewing

#### 4.3.2 Contributor (Activated User)
• Create and edit own recipes
• Submit recipes for approval
• Like and favorite recipes
• Write reviews and ratings
• Access search history
• View profile and statistics

#### 4.3.3 Guest (No Sign-in / Pending or Suspended Users)
• Browse published recipes
• Search published recipes
• View recipe detail pages and read reviews/ratings
• No interaction privileges (no likes, favorites, or reviews)

## 5. Data Models

### 5.1 Entity 1: User
Fields: id, username, firstName, lastName, email, password, birthday, role, status, joinedDate, lastActive, avatar, bio, location, cookingLevel, favorites, viewedRecipes, searchHistory

Operations: Create – User registration
          Read – View own profile, view user by ID, list all users (admin only)
          Update – Update own profile, Update user status (admin only)
          Delete – Delete user accounts (admin only)

### 5.2 Entity 2: Recipe
Fields: id, title, description, categories, ingredients, instructions, prepTime, cookTime, servings, difficulty, image, authorID, status, createdAt, UpdatedAt, views, likes

Operations: Create – Submit recipes with status 'pending'
          Read – View recipe details, List recipes with filters, Search recipes
          Update – Edit by recipe author, Admin approves/rejects recipes, Record views, Likes/unlikes recipe
          Delete – Delete recipes by admins or author

### 5.3 Entity 3: Review
Fields: id, recipeId, userId, rating, comment, createdAt, updatedAt

Operations: Create – Submit a review (active users only, one review per user per recipe)
         Read – View all reviews for a recipe, view user's own reviews
         Update – Edit own review
         Delete – Delete own review (owner or admin)

### 5.4 Entity 4: Activity Log
Fields: id, adminId, action, entityType, entityId, actionDetails, createdAt

Operations: Create – Automatically log admin actions (system internal)
         Read – View activity logs (admin only, with optional filters)
         Update – Not applicable (immutable)
         Delete – Not applicable (permanent audit trail)

### 5.5 Entity 5: Daily Stats
Fields: id, date, dailyActiveUsers, dailyViews, publishedRecipes, pendingRecipes, totalUsers, createdAt, updatedAt

Operations: Create – Automatically create new daily entry (system internal)
         Read – View daily statistics (admin dashboard, with date range filter)
         Update – Incrementally update counts during day (system internal)
         Delete – Not applicable (historical data preserved)

## 6. Technology Stack

### Frontend:
• ReactJS
• React Router DOM
• Vite
• Tailwind CSS
• Lucide React

### Backend:
• Next.js
• Next.js API Routes
• Next.js Middleware
• bcrypt
• JWT

### Database:
• MongoDB Atlas
• Mongoose ODM
• MongoDB Aggregation Framework

### Deployment:
• Azure App Service
• Azure Storage
• Azure Key Vault
• Azure Application Insights

### Development Tools:
• ESLint
• Git & GitHub
• Pnpm
• Figma
• Google Stitch
• Notion
• Visual Studio Code

## 7. Expected Outcomes

The completed Kitchen Odyssey platform is aimed at delivering a moderated, user-friendly recipe sharing site that enhances discovery and contribution while ensuring content quality. Key outcomes include high user retention via engagement tools, efficient admin oversight, and scalables analytics for monitoring.
