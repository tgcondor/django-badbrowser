
__version__ = "1.0.7"

def check_user_agent(user_agent, requirements):
    import httpagentparser
    from pkg_resources import parse_version
    
    if not user_agent:
        return True
    
    if not requirements:
        return True
    
    if type(user_agent) == dict:
        parsed = user_agent
    else:
        parsed = httpagentparser.detect(user_agent)
    
    if "browser" not in parsed:
        return True
    
    if "name" not in parsed["browser"]:
        return True
    
    if "version" not in parsed["browser"]:
        return True
    
    user_browser = parsed["browser"]["name"].lower()
    user_browser_version = parsed["browser"]["version"]
    
    for browser, browser_version in requirements:
        if not browser_version:
            return False
        if user_browser == browser.lower():
            if cmp(parse_version(browser_version), parse_version(user_browser_version)) <= 0:
                return True
    
    return False
