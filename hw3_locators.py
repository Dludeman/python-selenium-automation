#Amazon logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

#Create account heading
driver.find_element(By.XPATH, "//h1[text()='Create account']")

#"Name" input field
driver.find_element(By.ID, 'ap_customer_name')

#"Email" input field
driver.find_element(By.ID, 'ap_email')

#"password" input field
driver.find_element(By.ID, 'ap_password')

#"password requirement" alert box
driver.find_element(By.CSS_SELECTOR, 'div.a-alert-container')

#"Re-enter password" box
driver.find_element(By.ID, 'ap_password_check')

#"Continue" button
driver.find_element(By.ID, 'continue')

#"Conditions of use" link
driver.find_element(By.CSS_SELECTOR, "[href*='condition_of_use']")

#"Privacy Notic" link
driver.find_element(By.CSS_SELECTOR, "[href*='privacy_notice']")

#"Sign in" link
driver.find_element(By.CSS_SELECTOR, "[href*='signin']")




driver.find_element(By.XPATH, "//a[text()='Best Sellers']")