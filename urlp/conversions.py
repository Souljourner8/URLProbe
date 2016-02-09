"""
Know the differences between bytes, str, and unicode

Unicode and str instances seem to be the same type when a str only contains 7-bit ASCII characters.

    - You can combine such s str and unicode together using the + operator.
    - You can compare such str and unicode instances using equality and inequality operators.
    - You can use unicode instances for format strings like '%s'.

You can often pass a str or unicode instance to a function expecting one or the other and things will just work
(as long as you're only dealing with 7-bit ASCII)
"""


def to_unicode(unicode_or_str):
    """
    Takes a str or unicode and always returns a unicode
    :param unicode_or_str: str or unicode
    :return: unicode
    """
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value    # Instance of unicode


def to_str(unicode_or_str):
    """
    Takes str or unicode and always returns a str
    :param unicode_or_str: str or unicode
    :return: str
    """
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value    # Instance of str