import { defineConfig } from '@playwright/test'

export default defineConfig({
	retries: 0,
	use: { baseURL: 'http://localhost:5173' },
})