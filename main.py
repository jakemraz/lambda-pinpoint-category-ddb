import lambda_campaign_push




if __name__ == "__main__":

    event = {
        "segment": "first",
        "title": "Hello {{User.UserId}}",
        "message": "Let's introduce new product Echo Bud!",
        "category": "IT",
        "icon": "https://apprecs.org/ios/images/app-icons/256/6d/580990573.jpg",
        "image": "https://pplware.sapo.pt/wp-content/uploads/2019/09/Amazon_Echo_Buds_02.jpg"
    }

    lambda_campaign_push.lambda_handler(event, None)


    pass