import React, { useEffect, useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/Card';
import { storage } from '../../lib/storage';
import { Users, FileText, Activity, UserPlus, ChefHat, Eye } from 'lucide-react';

// StatCard component moved outside to prevent recreation on each render
const StatCard = ({ title, value, icon, subtext }) => {
    const Icon = icon;
    return (
        <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium text-cool-gray-60">
                    {title}
                </CardTitle>
                <Icon className="h-4 w-4 text-cool-gray-60" />
            </CardHeader>
            <CardContent>
                <div className="text-2xl font-bold">{value}</div>
                {subtext && <p className="text-xs text-cool-gray-60 mt-1">{subtext}</p>}
            </CardContent>
        </Card>
    );
};

export function AdminStats() {
    const [stats, setStats] = useState({
        totalUsers: 0,
        newUsersToday: 0,
        contributors: 0,
        newContributorsToday: 0,
        publishedRecipes: 0,
        pendingRecipes: 0,
        dailyViews: 0,
        dailyActiveUsers: 0,
        recentActivity: []
    });

    useEffect(() => {
        const loadStats = () => {
            const users = storage.getUsers();
            const recipes = storage.getRecipes();
            const newUsersToday = storage.getNewUsersToday();
            const newContributorsToday = storage.getNewContributorsToday();
            const dailyActiveUsers = storage.getDailyActiveUsers();
            // Contributors should exclude users with 'pending' status
            setStats({
                totalUsers: users.filter(u => u.role !== 'admin').length,
                newUsersToday: newUsersToday.length,
                contributors: users.filter(u => u.role === 'user' && u.status !== 'pending').length,
                newContributorsToday: newContributorsToday.filter(u => u.status !== 'pending').length,
                publishedRecipes: recipes.filter(r => r.status === 'published').length,
                pendingRecipes: recipes.filter(r => r.status === 'pending').length,
                dailyViews: storage.getDailyViews(),
                dailyActiveUsers: dailyActiveUsers.length,
                recentActivity: storage.getRecentActivity(5)
            });
        };

        loadStats();
        const interval = setInterval(loadStats, 30000);
        const handleStatsUpdate = () => loadStats();
        window.addEventListener('statsUpdated', handleStatsUpdate);
        window.addEventListener('recipeUpdated', handleStatsUpdate);
        window.addEventListener('userUpdated', handleStatsUpdate);

        return () => {
            clearInterval(interval);
            window.removeEventListener('statsUpdated', handleStatsUpdate);
            window.removeEventListener('recipeUpdated', handleStatsUpdate);
            window.removeEventListener('userUpdated', handleStatsUpdate);
        };
    }, []);

    return (
        <div className="space-y-6">
            <div>
                <h1 className="text-3xl font-bold tracking-tight text-cool-gray-90">Dashboard</h1>
                <p className="text-cool-gray-60">Overview of system performance and activity.</p>
            </div>

            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
                <StatCard title="Total Users" value={stats.totalUsers} icon={Users} subtext="All registered users" />
                <StatCard title="New Users Today" value={stats.newUsersToday} icon={UserPlus} subtext="Joined today" />
                <StatCard title="Total Contributors" value={stats.contributors} icon={ChefHat} subtext="Recipe creators" />
                <StatCard title="New Contributors Today" value={stats.newContributorsToday} icon={UserPlus} subtext="New recipe creators" />
            </div>

            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
                <StatCard title="Published Recipes" value={stats.publishedRecipes} icon={FileText} subtext="Approved recipes" />
                <StatCard title="Pending Recipes" value={stats.pendingRecipes} icon={FileText} subtext="Awaiting approval" />
                <StatCard title="Daily Views" value={stats.dailyViews} icon={Eye} subtext="Total recipe views" />
                <StatCard title="Daily Active Users" value={stats.dailyActiveUsers} icon={Activity} subtext="Active today (DAU)" />
            </div>

            <div className="grid gap-4 md:grid-cols-2">
                {/* Quick placeholder for charts/trends */}
                <Card className="col-span-1">
                    <CardHeader>
                        <CardTitle>Recent Activity</CardTitle>
                    </CardHeader>
                    <CardContent>
                        <div className="space-y-2 text-sm text-cool-gray-60">
                            {stats.recentActivity.length ? (
                                stats.recentActivity.map((activity, index) => (
                                    <div key={`${activity.type}-${activity.time}-${index}`} className="flex items-start justify-between gap-4">
                                        <span>{activity.text}</span>
                                        <span className="whitespace-nowrap text-xs text-cool-gray-50">
                                            {new Date(activity.time).toLocaleString()}
                                        </span>
                                    </div>
                                ))
                            ) : (
                                <p>No recent activity yet.</p>
                            )}
                        </div>
                    </CardContent>
                </Card>
                <Card className="col-span-1">
                    <CardHeader>
                        <CardTitle>System Health</CardTitle>
                    </CardHeader>
                    <CardContent>
                        <div className="flex items-center gap-2">
                            <div className="h-2 w-2 rounded-full bg-green-500"></div>
                            <span className="text-sm font-medium">All systems operational</span>
                        </div>
                    </CardContent>
                </Card>
            </div>
        </div>
    );
}
