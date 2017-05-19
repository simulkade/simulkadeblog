# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1495224529.3132484
_enable_loop = True
_template_filename = 'themes/lanyon/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_feedlinks', 'late_load_js', 'html_translations', 'html_stylesheets', 'html_headstart']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>\n            <script src="/assets/js/all.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if use_cdn:
                __M_writer('            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/jquery.min.js"></script>\n')
            __M_writer('        <script src="/assets/js/moment-with-locales.min.js"></script>\n        <script src="/assets/js/fancydates.js"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <ul class="translations">\n')
        for langname in translations.keys():
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            __M_writer('        <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/poole.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/lanyon.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        __M_writer('    <link rel="stylesheet" href="//fonts.googleapis.com/css?family=PT+Serif:400,400italic,700|PT+Sans:400">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_feedlinks():
            return render_html_feedlinks(context)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        description = context.get('description', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        striphtml = context.get('striphtml', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        title = context.get('title', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n    <title>')
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\n\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n')
        if permalink:
            __M_writer('      <link rel="canonical" href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        __M_writer('\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/lanyon/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 61, "23": 81, "24": 96, "25": 119, "26": 129, "32": 98, "42": 98, "43": 99, "44": 100, "45": 100, "46": 100, "47": 101, "48": 102, "49": 103, "50": 104, "51": 104, "52": 104, "53": 104, "54": 104, "55": 106, "56": 107, "57": 107, "58": 107, "59": 110, "60": 111, "61": 112, "62": 113, "63": 113, "64": 113, "65": 113, "66": 113, "67": 115, "68": 116, "69": 116, "70": 116, "76": 63, "83": 63, "84": 64, "85": 65, "86": 66, "87": 68, "88": 69, "89": 71, "90": 72, "91": 73, "92": 74, "93": 75, "94": 77, "95": 80, "96": 80, "97": 80, "103": 121, "112": 121, "113": 123, "114": 124, "115": 125, "116": 125, "117": 125, "118": 125, "119": 125, "120": 125, "121": 125, "122": 128, "128": 83, "134": 83, "135": 84, "136": 85, "137": 86, "138": 87, "139": 91, "140": 92, "141": 95, "147": 3, "174": 3, "175": 6, "176": 7, "177": 8, "178": 10, "179": 11, "180": 13, "181": 14, "182": 15, "183": 17, "184": 18, "185": 21, "186": 21, "187": 21, "188": 24, "189": 25, "190": 25, "191": 25, "192": 27, "193": 28, "194": 28, "195": 28, "196": 28, "197": 30, "198": 30, "199": 31, "200": 31, "201": 32, "202": 33, "203": 33, "204": 33, "205": 35, "206": 36, "207": 37, "208": 38, "209": 38, "210": 38, "211": 38, "212": 38, "213": 38, "214": 38, "215": 41, "216": 42, "217": 43, "218": 43, "219": 43, "220": 45, "221": 46, "222": 47, "223": 47, "224": 47, "225": 49, "226": 50, "227": 50, "228": 50, "229": 52, "230": 53, "231": 53, "232": 54, "233": 55, "234": 56, "235": 57, "236": 57, "237": 57, "238": 59, "239": 60, "240": 60, "246": 240}}
__M_END_METADATA
"""
