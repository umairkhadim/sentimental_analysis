from django.shortcuts import render

# Create your views here.


# @login_required(login_url='login')
def customer_dashboard(request):
    # reddit = praw.Reddit(client_id='ISnOA13qK99q4A',
    #                      client_secret='cEKVwb65zJJoejN6YphDRamyHycdHA',
    #                      user_agent='my user agent')
    #
    # # to find the top most submission in the subreddit "HEALTH"
    # subreddit = reddit.subreddit('HEALTH')

    # for submission in subreddit.top(limit=5):
    #
    #     dt = datetime.datetime.fromtimestamp(float(submission.created_utc))
    #     print(dt)
    #     tweets = Tweets(create_time=dt, description=submission.title)
    #     tweets.save()
    # items_submission = ItemSubmissionDate.objects.filter(customer=request.user).order_by('-create_date')[:5]
    # sub_reddit = Tweets.objects.all()[:5]
    context = {
        # 'sub_reddit': sub_reddit,
        # "table": items_submission,

    }
    return render(request, 'customer/dashboard.html', context)
