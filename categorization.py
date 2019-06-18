def categorization():
    category_filename = f'{blog.output_path}/categories'
    category_path = Path(category_filename)
    category_path.mkdir(parents=True, exist_ok=True)
    write_page(f'{category_path}/all.html',
            Page(template='categories.html',
            topic_list=[c for c in blog.categories]).html)

    for category in blog.categories:
        write_page(f'{category_path}/{category}.html',
                Page(template='blog_list.html',
                    post_list=blog.categories[category],
                    output_path=blog.output_path).html)
        feed_gen(
                blog,
                page_filter=blog.categories[category],
                output_path=category_path,
                name=category,
                )

    tag_path = Path(f'{blog.output_path}/tag')
    tag_path.mkdir(parents=True, exist_ok=True)
    write_page(f'{tag_path}/all.html', Page(template='categories.html',
        topic_list=[t for t in blog.tags]).html)

    for tag in blog.tags:
        write_page(f'{tag_path}/{tag}.html',
                Page(template='blog_list.html',
                post_list=blog.tags[tag],
                output_path=blog.output_path).html)



