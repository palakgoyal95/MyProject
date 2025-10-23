// tailwind.config.js

/** @type {import('tailwindcss').Config} */
module.exports = {
  // CRITICAL: Point Tailwind to your Django templates
  content: [
    "./templates/**/*.html", // Project-level templates
    "./**/templates/**/*.html", // App-level templates
    // Add paths to any other files (e.g., .js) that use Tailwind classes
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
