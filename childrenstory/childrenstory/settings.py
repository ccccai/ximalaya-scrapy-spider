BOT_NAME = 'childrenstory'

SPIDER_MODULES = ['childrenstory.spiders']
NEWSPIDER_MODULE = 'childrenstory.spiders'

COOKIES_ENABLED = False

ITEM_PIPELINES = {
	'childrenstory.pipelines.XimalayaMongoPipeline':300,
	# 'childrenstory.pipelines.Storymp3Pipeline':300,
    # 'childrenstory.pipelines.StoryimgPipeline':300,
    # 'childrenstory.pipelines.StorytitlePipeline':300
}

IMAGES_STORE ='D:'
DOWNLOAD_DELAY = 0.3

MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
MONGODB_NAME = "Spider"
MONGODB_TABLE = "ximalaya"