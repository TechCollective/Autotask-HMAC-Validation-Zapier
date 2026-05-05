# How to create a AutoTask generated webhook that uses HMAC authentication for Zapier

In Zapier:
1. Create a new Zap in Zapier
2. Add a Webhooks by Zapier trigger
3. Select "Catch *Raw* Hook" in the events area
4. Copy the webhook URL

In the Autotask-Webhook-Manager:
1. Create a new Webhook
2. Add a new random string for the secret key
3. Copy the secret key
4. Insert the Zapier provided webhook url into the Target URL and Deactivation URL fields
5. Give the webhook a name, select the event subscriptions and mark it as "Active"
6. Save the webhook
7. Select the "Configure Fields" icon and add at least one field.
8. Verify that the "Ready" section is checked.
9. In Autotask, do whatever is necessary to trigger a webhook.

In Zapier:
1. Add a new "Code" step
2. Copy the python script to the code step
3. Add the following input data entries to the code step:
    - raw_body: The raw body of the webhook (in the "value" type /Raw and then select the "Raw Body" entry from the list below)
    - hook: The hook signature from the webhook (in the "value" type /Headers and select "Headers X Hook Signature from the list below)
    - secret_key: The secret key from Autotask (in the "value" type in the actual key you gave AutoTask))
5. If the webhook is valid, the Zap will continue
6. If the webhook is invalid, the Zap will stop

Continue adding any additional steps to your Zap here.
