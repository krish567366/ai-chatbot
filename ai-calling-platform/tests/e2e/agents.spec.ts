import { test, expect } from '@playwright/test'

test('agents page loads', async ({ page }) => {
	await page.goto('/agents')
	await expect(page.locator('text=Agents')).toBeVisible()
})