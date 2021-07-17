def category_image(instance, filename):
    return 'categories/{0}/{1}'.format(instance.id, filename)

def product_image(instance, filename):
    return 'products/{0}/{1}'.format(instance.id, filename)

def author_image(instance, filename):
    return 'authors/{0}/{1}'.format(instance.id, filename)

def custom_slugify(slug):
    slug = slug.replace(" ", "-")
    slug = slug.replace(",", "-")
    slug = slug.replace("(", "-")
    slug = slug.replace(")", "")
    slug = slug.replace("؟", "")
    return slug
