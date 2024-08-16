# Import necessary libraries
from facebookbusiness.api import FacebookAdsApi

# Configure API access
access_token = "EAAOtC2TF0KIBOyuZBfpMnZCvROl6ZCIZBOlGJT4eloJsPYcZCVCF54NgaZBvzXOPfPAocWobsRjLrLEvHwhX6b3nfA9OLRdg1DRfY9VJAoKQeWGPCWD0wWuzgV7wIdbS1iMZC28vs5AK7OYRkD2SPj0kCZB6vxNuqZATzNAXoZAYAXXc8oA4EhKFVO9YibuXrGrBDCelrodoA83xQ9C33H0sbVkVrqqPgZD"
api = FacebookAdsApi(access_token=access_token)

# Specify target ad account ID
target_account_id = "287556187600900"

# Request access to the target account
api.business_management.request_business_asset_access(
    business_id=target_account_id,
    permissions=["ads_read"],
)

# Check the request status
request_info = api.business_management.get_business_asset_access_request(
    request_id="1034689377063074"
)

if request_info["status"] == "approved":
    # Access the target ad account data
    account = api.get_account(account_id=target_account_id)
    campaigns = account.get_campaigns()
    print(f"Campaigns in {account['name']}:")
    for campaign in campaigns:
        print(f"\t- {campaign['name']}")
else:
    print(f"Access request not yet approved or denied.")

