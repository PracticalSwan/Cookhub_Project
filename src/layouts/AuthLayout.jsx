import React from 'react';
import { Outlet } from 'react-router-dom';
import Logo from '../assets/Logo.png';

export function AuthLayout() {
    return (
        <div className="min-h-screen grid lg:grid-cols-5">
            {/* Left: Form */}
            <div className="flex items-center justify-center p-8 bg-cool-gray-10 lg:col-span-3">
                <div className="w-full max-w-sm space-y-6">
                    <div className="flex justify-center mb-8">
                        <img src={Logo} alt="CookHub Logo" className="h-16 w-auto" />
                    </div>
                    <Outlet />
                </div>
            </div>

            {/* Right: Branding/Image */}
            <div className="hidden lg:flex lg:col-span-2 flex-col bg-cool-gray-90 text-white p-12 relative overflow-hidden">
                <div className="z-10 flex-1 flex flex-col items-center justify-center gap-6">
                    <img src={Logo} alt="CookHub Logo" className="h-32 w-auto" />
                    <h1 className="text-5xl font-bold">CookHub</h1>
                </div>
                {/* Abstract Background Decoration */}
                <div className="absolute top-0 right-0 -mr-20 -mt-20 w-[500px] h-[500px] bg-white/5 rounded-full blur-3xl" />
                <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-[400px] h-[400px] bg-white/5 rounded-full blur-3xl" />
            </div>
        </div>
    );
}
