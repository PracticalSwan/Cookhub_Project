import { clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs) {
    return twMerge(clsx(inputs))
}

export const RECIPE_CATEGORIES = [
    'Breakfast',
    'Lunch',
    'Dinner',
    'Dessert',
    'Italian',
    'Asian',
    'Health'
]

export const RECIPE_DIFFICULTIES = [
    'Easy',
    'Medium',
    'Hard'
]

export const normalizeCategories = (value) => {
    if (Array.isArray(value)) return value.filter(Boolean)
    if (typeof value === 'string' && value.trim()) return [value]
    return []
}
