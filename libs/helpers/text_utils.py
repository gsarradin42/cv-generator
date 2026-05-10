def gen_tag(tagname, content, attr_list={}, new_line=False):
    attr_list_st = (
        " " + " ".join([f"{k}={v}" for k, v in attr_list]) if attr_list else ""
    )
    nl_st = "\n" if new_line else ""
    return f"<{tagname}{attr_list_st}>{nl_st}{content}{nl_st}</{tagname}>"


def gen_tag_nl(tagname, content, attr_list={}):
    return gen_tag(tagname, content, attr_list, True)


def indent_line(line, amount=1):
    return (" " * amount * 4) + line


def indent_multiple_line(text, amount=1):
    return (
        "\n"
        + "\n".join([indent_line(line, amount) for line in text])
        + "\n"
        + indent_line("", amount - 1)
    )


def category_list_to_html_table(cat_list, cat_key: str, lst_key: str):
    return (
        "<table>\n"
        + "\n".join(
            [
                indent_line(
                    f"<tr><td>{category.get(cat_key)}</td><td>{
                        ', '.join(category.get(lst_key))
                    }</td></tr>",
                    1,
                )
                for category in cat_list
            ]
        )
        + "\n</table>"
    )


def category_list_to_html_table_v2(cat_list, cat_key: str, lst_key: str):
    return gen_tag_nl(
        "table",
        "\n".join(
            [
                indent_line(
                    gen_tag(
                        "tr",
                        gen_tag("td", cat.get(cat_key))
                        # + gen_tag("td", cat.get(lst_key)),
                        + gen_tag("td", ", ".join(cat.get(lst_key))),
                    )
                )
                for cat in cat_list
            ]
        ),
    )
