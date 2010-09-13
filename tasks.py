from celery.decorators import task


@task
def github_hook(repo, **kw):
    log = github_hook.get_logger(**kw)
    log.info('Running task with repo %s!' % repo)