import pyramid_handlers
from crawler_app.controllers.base_controller import BaseController
# from crawler_app.infrastructure.supressor import suppress


class VizController(BaseController):

    @pyramid_handlers.action(renderer='templates/visualization/viz.pt')
    def index(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, must login")
            self.redirect('/home/signin')

        graph = """{"url": "https://www.cas-donoghue.org/", "children": [{"url": "https://donoghuc.github.io", "children": [{"url": "https://www.cas-donoghue.org", "domain": "www.cas-donoghue.org"}, {"url": "https://www.linkedin.com/in/casadilla/", "domain": "www.linkedin.com"}, {"url": "https://github.com/donoghuc", "domain": "github.com"}, {"url": "https://stackoverflow.com/users/9034974/cas-donoghue?tab=profile", "domain": "stackoverflow.com"}, {"url": "https://www.cas-donoghue.org", "domain": "www.cas-donoghue.org"}, {"url": "https://talkpython.fm/", "domain": "talkpython.fm"}, {"url": "https://pythonbytes.fm/", "domain": "pythonbytes.fm"}, {"url": "https://www.podcastinit.com/", "domain": "www.podcastinit.com"}, {"url": "http://testandcode.com/", "domain": "testandcode.com"}, {"url": "https://changelog.com/", "domain": "changelog.com"}, {"url": "https://dataskeptic.com/", "domain": "dataskeptic.com"}, {"url": "https://www.dataengineeringpodcast.com/", "domain": "www.dataengineeringpodcast.com"}, {"url": "https://gimletmedia.com/science-vs/", "domain": "gimletmedia.com"}], "domain": "donoghuc.github.io"}, {"url": "https://github.com/donoghuc/casadilla_web", "children": [{"url": "https://github.com/", "domain": "github.com"}, {"url": "https://www.cas-donoghue.org", "domain": "www.cas-donoghue.org"}, {"url": "https://help.github.com/articles/which-remote-url-should-i-use", "domain": "help.github.com"}, {"url": "https://www.cas-donoghue.org", "domain": "www.cas-donoghue.org"}, {"url": "https://help.github.com/articles/github-terms-of-service/", "domain": "help.github.com"}, {"url": "https://github.com/site/privacy", "domain": "github.com"}, {"url": "https://help.github.com/articles/github-security/", "domain": "help.github.com"}, {"url": "https://status.github.com/", "domain": "status.github.com"}, {"url": "https://help.github.com", "domain": "help.github.com"}, {"url": "https://github.com", "domain": "github.com"}, {"url": "https://github.com/contact", "domain": "github.com"}, {"url": "https://developer.github.com", "domain": "developer.github.com"}, {"url": "https://training.github.com", "domain": "training.github.com"}, {"url": "https://shop.github.com", "domain": "shop.github.com"}, {"url": "https://github.com/blog", "domain": "github.com"}, {"url": "https://github.com/about", "domain": "github.com"}], "domain": "github.com"}, {"url": "https://twitter.com/mkennedy", "children": [{"url": "https://twitter.com/signup", "domain": "twitter.com"}, {"url": "https://pbs.twimg.com/profile_images/654042416840855552/2fy3qvpo_400x400.jpg", "domain": "pbs.twimg.com"}, {"url": "https://pbs.twimg.com/profile_images/654042416840855552/2fy3qvpo.jpg", "domain": "pbs.twimg.com"}, {"url": "https://t.co/DRQ8CqQ2eF", "domain": "t.co"}, {"url": "https://t.co/3wbDRhqFW7", "domain": "t.co"}, {"url": "https://t.co/V7ueFhogSm", "domain": "t.co"}, {"url": "https://t.co/OHvMOIaxJV", "domain": "t.co"}, {"url": "https://t.co/uodtGYg8af", "domain": "t.co"}, {"url": "https://t.co/eONaeDZiHU", "domain": "t.co"}, {"url": "https://t.co/PId2T0324b", "domain": "t.co"}, {"url": "https://t.co/wZIKp0ZGpM", "domain": "t.co"}, {"url": "https://t.co/c3DMxQQRmc", "domain": "t.co"}, {"url": "https://t.co/iymVMS3wc0", "domain": "t.co"}, {"url": "https://t.co/XDpIGulhmA", "domain": "t.co"}, {"url": "https://t.co/qoDPkEkJya", "domain": "t.co"}, {"url": "https://t.co/XBHinmr7oV", "domain": "t.co"}, {"url": "https://t.co/OUNYWG9MLM", "domain": "t.co"}, {"url": "https://t.co/iEVORfbUGm", "domain": "t.co"}, {"url": "https://t.co/FeNhN9W8pp", "domain": "t.co"}, {"url": "https://t.co/fRCSbPZdH1", "domain": "t.co"}, {"url": "https://t.co/bfPCPoOtXS", "domain": "t.co"}, {"url": "https://t.co/zgKKLv2IIf", "domain": "t.co"}, {"url": "https://t.co/OUDQqjhbJH", "domain": "t.co"}, {"url": "https://t.co/JEOvxWAfw2", "domain": "t.co"}, {"url": "https://t.co/dqwK0brYYx", "domain": "t.co"}, {"url": "https://t.co/TEtprtt9cT", "domain": "t.co"}, {"url": "https://t.co/HbdHQ3wuds", "domain": "t.co"}, {"url": "https://t.co/NigaENGla3", "domain": "t.co"}, {"url": "http://status.twitter.com", "domain": "status.twitter.com"}, {"url": "https://twitter.com/signup", "domain": "twitter.com"}, {"url": "http://support.twitter.com/forums/26810/entries/78525", "domain": "support.twitter.com"}, {"url": "https://dev.twitter.com/web/embedded-tweets", "domain": "dev.twitter.com"}, {"url": "https://dev.twitter.com/web/embedded-tweets", "domain": "dev.twitter.com"}, {"url": "https://dev.twitter.com/overview/terms/agreement", "domain": "dev.twitter.com"}, {"url": "https://dev.twitter.com/overview/terms/policy", "domain": "dev.twitter.com"}, {"url": "https://twitter.com/signup", "domain": "twitter.com"}, {"url": "https://twitter.com/signup", "domain": "twitter.com"}, {"url": "http://support.twitter.com/articles/14226-how-to-find-your-twitter-short-code-or-long-code", "domain": "support.twitter.com"}], "domain": "twitter.com"}, {"url": "https://talkpython.fm", "children": [{"url": "https://training.talkpython.fm/", "domain": "training.talkpython.fm"}, {"url": "https://www.patreon.com/mkennedy", "domain": "www.patreon.com"}, {"url": "https://rollbar.com/talkpythontome", "domain": "rollbar.com"}, {"url": "https://twitter.com/talkpython", "domain": "twitter.com"}, {"url": "https://backtracks.fm/talkpython/r/talkpython.fm/episodes/download/150/150-technical-lessons-learned-from-pythonic-refactoring.mp3?s=1", "domain": "backtracks.fm"}, {"url": "https://training.talkpython.fm/courses/explore_python_jumpstart/python-language-jumpstart-building-10-apps", "domain": "training.talkpython.fm"}, {"url": "https://training.talkpython.fm/courses/explore_pythonic_code/write-pythonic-code-like-a-seasoned-developer", "domain": "training.talkpython.fm"}, {"url": "https://training.talkpython.fm/courses/explore_entrepreneurs/python-for-entrepreneurs-build-and-launch-your-online-business", "domain": "training.talkpython.fm"}, {"url": "https://itunes.apple.com/us/podcast/talk-python-to-me-python-conversations/id979020229", "domain": "itunes.apple.com"}, {"url": "https://gitter.im/talk-python/Lobby", "domain": "gitter.im"}, {"url": "https://gitter.im/talk-python", "domain": "gitter.im"}, {"url": "https://gitter.im/talk-python", "domain": "gitter.im"}, {"url": "https://pythonbytes.fm/", "domain": "pythonbytes.fm"}, {"url": "https://pythonbytes.fm/", "domain": "pythonbytes.fm"}, {"url": "https://pythonbytes.fm/", "domain": "pythonbytes.fm"}, {"url": "http://www.pythongear.com/products/talk-python-to-me-shirt?utm_source=talkpythonweb&utm_campaign=web_direct", "domain": "www.pythongear.com"}, {"url": "https://www.stickermule.com/user/1070815159/stickers", "domain": "www.stickermule.com"}, {"url": "http://www.pythongear.com/products/talk-python-to-me-shirt?utm_source=talkpythonweb&utm_campaign=web_direct", "domain": "www.pythongear.com"}, {"url": "https://www.stickermule.com/user/1070815159/stickers", "domain": "www.stickermule.com"}, {"url": "https://www.patreon.com/mkennedy", "domain": "www.patreon.com"}, {"url": "https://cash.me/$mkennedy", "domain": "cash.me"}, {"url": "https://www.patreon.com/mkennedy", "domain": "www.patreon.com"}, {"url": "http://blog.michaelckennedy.net", "domain": "blog.michaelckennedy.net"}, {"url": "https://twitter.com/mkennedy", "domain": "twitter.com"}, {"url": "https://twitter.com/TalkPython/lists/show-guests", "domain": "twitter.com"}, {"url": "https://twitter.com/TalkPython/lists/show-guests", "domain": "twitter.com"}, {"url": "https://twitter.com/TalkPython", "domain": "twitter.com"}, {"url": "https://twitter.com/mkennedy", "domain": "twitter.com"}, {"url": "https://facebook.com/talkpython", "domain": "facebook.com"}, {"url": "https://twitter.com/talkpython", "domain": "twitter.com"}, {"url": "https://itunes.apple.com/us/podcast/talk-python-to-me-python-conversations/id979020229", "domain": "itunes.apple.com"}, {"url": "https://goo.gl/app/playmusic?ibi=com.google.PlayMusic&isi=691797987&ius=googleplaymusic&link=https://play.google.com/music/m/Ili2egodifhl6zqriqcw5m2cjpy?t%3DTalk_Python_To_Me_-_Python_conversations_for_passionate_developers", "domain": "goo.gl"}, {"url": "https://training.talkpython.fm/", "domain": "training.talkpython.fm"}, {"url": "https://twitter.com/TalkPython", "domain": "twitter.com"}, {"url": "https://www.facebook.com/talkpython", "domain": "www.facebook.com"}, {"url": "https://www.youtube.com/channel/UCKPSmMfDsXTKrCZApukcJ7A", "domain": "www.youtube.com"}, {"url": "https://soundcloud.com/talkpython", "domain": "soundcloud.com"}, {"url": "https://plus.google.com/u/0/b/107602463704502246507/+Talkpythontomepodcast/posts", "domain": "plus.google.com"}, {"url": "http://pdxwebproperties.com/", "domain": "pdxwebproperties.com"}], "domain": "talkpython.fm"}, {"url": "https://github.com/donoghuc", "children": [{"url": "https://github.com/", "domain": "github.com"}, {"url": "https://avatars3.githubusercontent.com/u/15354214?s=400&v=4", "domain": "avatars3.githubusercontent.com"}, {"url": "https://www.cas-donoghue.org", "domain": "www.cas-donoghue.org"}, {"url": "https://help.github.com/articles/why-are-my-contributions-not-showing-up-on-my-profile", "domain": "help.github.com"}, {"url": "https://help.github.com/categories/setting-up-and-managing-your-github-profile", "domain": "help.github.com"}, {"url": "https://help.github.com/articles/github-terms-of-service/", "domain": "help.github.com"}, {"url": "https://github.com/site/privacy", "domain": "github.com"}, {"url": "https://help.github.com/articles/github-security/", "domain": "help.github.com"}, {"url": "https://status.github.com/", "domain": "status.github.com"}, {"url": "https://help.github.com", "domain": "help.github.com"}, {"url": "https://github.com", "domain": "github.com"}, {"url": "https://github.com/contact", "domain": "github.com"}, {"url": "https://developer.github.com", "domain": "developer.github.com"}, {"url": "https://training.github.com", "domain": "training.github.com"}, {"url": "https://shop.github.com", "domain": "shop.github.com"}, {"url": "https://github.com/blog", "domain": "github.com"}, {"url": "https://github.com/about", "domain": "github.com"}], "domain": "github.com"}, {"url": "https://stackoverflow.com/users/9034974/cas-donoghue?tab=profile", "children": [{"url": "https://stackoverflow.com", "domain": "stackoverflow.com"}, {"url": "https://stackoverflow.com", "domain": "stackoverflow.com"}, {"url": "https://stackoverflow.com/help", "domain": "stackoverflow.com"}, {"url": "https://chat.stackoverflow.com", "domain": "chat.stackoverflow.com"}, {"url": "https://stackoverflow.com", "domain": "stackoverflow.com"}, {"url": "https://meta.stackoverflow.com", "domain": "meta.stackoverflow.com"}, {"url": "https://stackoverflow.com/users/signup?ssrc=site_switcher&returnurl=%2fusers%2fstory%2fcurrent&amp;utm_source=stackoverflow.com&amp;utm_medium=dev-story&amp;utm_campaign=signup-redirect", "domain": "stackoverflow.com"}, {"url": "https://stackoverflow.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fstackoverflow.com%2fusers%2f9034974%2fcas-donoghue%3ftab%3dprofile", "domain": "stackoverflow.com"}, {"url": "https://stackexchange.com/sites", "domain": "stackexchange.com"}, {"url": "https://stackoverflow.blog", "domain": "stackoverflow.blog"}, {"url": "https://meta.stackoverflow.com", "domain": "meta.stackoverflow.com"}, {"url": "https://stackoverflow.com/company/about", "domain": "stackoverflow.com"}, {"url": "https://www.stackoverflowbusiness.com/?ref=topbar_help", "domain": "www.stackoverflowbusiness.com"}, {"url": "https://stackexchange.com/users/?tab=inbox", "domain": "stackexchange.com"}, {"url": "https://stackexchange.com/users/?tab=reputation", "domain": "stackexchange.com"}, {"url": "https://stackexchange.com", "domain": "stackexchange.com"}, {"url": "https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fusers%2f9034974%2fcas-donoghue%3ftab%3dprofile", "domain": "stackoverflow.com"}, {"url": "https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent&utm_source=stackoverflow.com&utm_medium=dev-story&utm_campaign=signup-redirect", "domain": "stackoverflow.com"}, {"url": "https://meta.stackoverflow.com/users/9034974/cas-donoghue", "domain": "meta.stackoverflow.com"}, {"url": "https://stackexchange.com/users/12394439/cas-donoghue", "domain": "stackexchange.com"}, {"url": "https://stackoverflow.com/users/9034974/cas-donoghue", "domain": "stackoverflow.com"}, {"url": "https://www.sarepta.com/", "domain": "www.sarepta.com"}, {"url": "http://donoghuc.github.io", "domain": "donoghuc.github.io"}, {"url": "http://cas-donoghue.org", "domain": "cas-donoghue.org"}, {"url": "https://github.com/donoghuc", "domain": "github.com"}, {"url": "https://stackoverflow.com/users/9034974/", "domain": "stackoverflow.com"}, {"url": "https://stackoverflow.com", "domain": "stackoverflow.com"}, {"url": "https://stackoverflow.com", "domain": "stackoverflow.com"}, {"url": "https://stackoverflow.com/jobs", "domain": "stackoverflow.com"}, {"url": "https://stackoverflow.com/jobs/directory/developer-jobs", "domain": "stackoverflow.com"}, {"url": "https://stackoverflow.com/jobs/salary", "domain": "stackoverflow.com"}, {"url": "https://www.stackoverflowbusiness.com/?utm_source=so-footer&utm_medium=referral&utm_campaign=brand-activation&utm_term=sotob2b-footer-business-category", "domain": "www.stackoverflowbusiness.com"}, {"url": "https://www.stackoverflowbusiness.com/talent?utm_source=so-footer&utm_medium=referral&utm_campaign=brand-activation&utm_term=sotob2b-footer-talent", "domain": "www.stackoverflowbusiness.com"}, {"url": "https://www.stackoverflowbusiness.com/advertise?utm_source=so-footer&utm_medium=referral&utm_campaign=brand-activation&utm_term=sotob2b-footer-advertise", "domain": "www.stackoverflowbusiness.com"}, {"url": "https://www.stackoverflowbusiness.com/enterprise?utm_source=so-footer&utm_medium=referral&utm_campaign=brand-activation&utm_term=sotob2b-footer-enterprise", "domain": "www.stackoverflowbusiness.com"}, {"url": "https://stackoverflow.com/company/about", "domain": "stackoverflow.com"}, {"url": "https://stackoverflow.com/company/about", "domain": "stackoverflow.com"}, {"url": "https://stackoverflow.com/company/press", "domain": "stackoverflow.com"}, {"url": "https://stackoverflow.com/company/work-here", "domain": "stackoverflow.com"}, {"url": "https://stackexchange.com/legal", "domain": "stackexchange.com"}, {"url": "https://stackexchange.com/legal/privacy-policy", "domain": "stackexchange.com"}, {"url": "https://stackoverflow.com/company/contact", "domain": "stackoverflow.com"}, {"url": "https://stackexchange.com", "domain": "stackexchange.com"}, {"url": "https://stackoverflow.com", "domain": "stackoverflow.com"}, {"url": "https://serverfault.com", "domain": "serverfault.com"}, {"url": "https://superuser.com", "domain": "superuser.com"}, {"url": "https://webapps.stackexchange.com", "domain": "webapps.stackexchange.com"}, {"url": "https://askubuntu.com", "domain": "askubuntu.com"}, {"url": "https://webmasters.stackexchange.com", "domain": "webmasters.stackexchange.com"}, {"url": "https://gamedev.stackexchange.com", "domain": "gamedev.stackexchange.com"}, {"url": "https://tex.stackexchange.com", "domain": "tex.stackexchange.com"}, {"url": "https://softwareengineering.stackexchange.com", "domain": "softwareengineering.stackexchange.com"}, {"url": "https://unix.stackexchange.com", "domain": "unix.stackexchange.com"}, {"url": "https://apple.stackexchange.com", "domain": "apple.stackexchange.com"}, {"url": "https://wordpress.stackexchange.com", "domain": "wordpress.stackexchange.com"}, {"url": "https://gis.stackexchange.com", "domain": "gis.stackexchange.com"}, {"url": "https://electronics.stackexchange.com", "domain": "electronics.stackexchange.com"}, {"url": "https://android.stackexchange.com", "domain": "android.stackexchange.com"}, {"url": "https://security.stackexchange.com", "domain": "security.stackexchange.com"}, {"url": "https://dba.stackexchange.com", "domain": "dba.stackexchange.com"}, {"url": "https://drupal.stackexchange.com", "domain": "drupal.stackexchange.com"}, {"url": "https://sharepoint.stackexchange.com", "domain": "sharepoint.stackexchange.com"}, {"url": "https://ux.stackexchange.com", "domain": "ux.stackexchange.com"}, {"url": "https://mathematica.stackexchange.com", "domain": "mathematica.stackexchange.com"}, {"url": "https://salesforce.stackexchange.com", "domain": "salesforce.stackexchange.com"}, {"url": "https://expressionengine.stackexchange.com", "domain": "expressionengine.stackexchange.com"}, {"url": "https://pt.stackoverflow.com", "domain": "pt.stackoverflow.com"}, {"url": "https://blender.stackexchange.com", "domain": "blender.stackexchange.com"}, {"url": "https://networkengineering.stackexchange.com", "domain": "networkengineering.stackexchange.com"}, {"url": "https://crypto.stackexchange.com", "domain": "crypto.stackexchange.com"}, {"url": "https://codereview.stackexchange.com", "domain": "codereview.stackexchange.com"}, {"url": "https://magento.stackexchange.com", "domain": "magento.stackexchange.com"}, {"url": "https://softwarerecs.stackexchange.com", "domain": "softwarerecs.stackexchange.com"}, {"url": "https://dsp.stackexchange.com", "domain": "dsp.stackexchange.com"}, {"url": "https://emacs.stackexchange.com", "domain": "emacs.stackexchange.com"}, {"url": "https://raspberrypi.stackexchange.com", "domain": "raspberrypi.stackexchange.com"}, {"url": "https://ru.stackoverflow.com", "domain": "ru.stackoverflow.com"}, {"url": "https://codegolf.stackexchange.com", "domain": "codegolf.stackexchange.com"}, {"url": "https://es.stackoverflow.com", "domain": "es.stackoverflow.com"}, {"url": "https://ethereum.stackexchange.com", "domain": "ethereum.stackexchange.com"}, {"url": "https://datascience.stackexchange.com", "domain": "datascience.stackexchange.com"}, {"url": "https://arduino.stackexchange.com", "domain": "arduino.stackexchange.com"}, {"url": "https://bitcoin.stackexchange.com", "domain": "bitcoin.stackexchange.com"}, {"url": "https://stackexchange.com/sites#technology", "domain": "stackexchange.com"}, {"url": "https://photo.stackexchange.com", "domain": "photo.stackexchange.com"}, {"url": "https://scifi.stackexchange.com", "domain": "scifi.stackexchange.com"}, {"url": "https://graphicdesign.stackexchange.com", "domain": "graphicdesign.stackexchange.com"}, {"url": "https://movies.stackexchange.com", "domain": "movies.stackexchange.com"}, {"url": "https://music.stackexchange.com", "domain": "music.stackexchange.com"}, {"url": "https://worldbuilding.stackexchange.com", "domain": "worldbuilding.stackexchange.com"}, {"url": "https://cooking.stackexchange.com", "domain": "cooking.stackexchange.com"}, {"url": "https://diy.stackexchange.com", "domain": "diy.stackexchange.com"}, {"url": "https://money.stackexchange.com", "domain": "money.stackexchange.com"}, {"url": "https://academia.stackexchange.com", "domain": "academia.stackexchange.com"}, {"url": "https://law.stackexchange.com", "domain": "law.stackexchange.com"}, {"url": "https://stackexchange.com/sites#lifearts", "domain": "stackexchange.com"}, {"url": "https://english.stackexchange.com", "domain": "english.stackexchange.com"}, {"url": "https://skeptics.stackexchange.com", "domain": "skeptics.stackexchange.com"}, {"url": "https://judaism.stackexchange.com", "domain": "judaism.stackexchange.com"}, {"url": "https://travel.stackexchange.com", "domain": "travel.stackexchange.com"}, {"url": "https://christianity.stackexchange.com", "domain": "christianity.stackexchange.com"}, {"url": "https://ell.stackexchange.com", "domain": "ell.stackexchange.com"}, {"url": "https://japanese.stackexchange.com", "domain": "japanese.stackexchange.com"}, {"url": "https://gaming.stackexchange.com", "domain": "gaming.stackexchange.com"}, {"url": "https://bicycles.stackexchange.com", "domain": "bicycles.stackexchange.com"}, {"url": "https://rpg.stackexchange.com", "domain": "rpg.stackexchange.com"}, {"url": "https://anime.stackexchange.com", "domain": "anime.stackexchange.com"}, {"url": "https://puzzling.stackexchange.com", "domain": "puzzling.stackexchange.com"}, {"url": "https://mechanics.stackexchange.com", "domain": "mechanics.stackexchange.com"}, {"url": "https://stackexchange.com/sites#culturerecreation", "domain": "stackexchange.com"}, {"url": "https://mathoverflow.net", "domain": "mathoverflow.net"}, {"url": "https://math.stackexchange.com", "domain": "math.stackexchange.com"}, {"url": "https://stats.stackexchange.com", "domain": "stats.stackexchange.com"}, {"url": "https://cstheory.stackexchange.com", "domain": "cstheory.stackexchange.com"}, {"url": "https://physics.stackexchange.com", "domain": "physics.stackexchange.com"}, {"url": "https://chemistry.stackexchange.com", "domain": "chemistry.stackexchange.com"}, {"url": "https://biology.stackexchange.com", "domain": "biology.stackexchange.com"}, {"url": "https://cs.stackexchange.com", "domain": "cs.stackexchange.com"}, {"url": "https://philosophy.stackexchange.com", "domain": "philosophy.stackexchange.com"}, {"url": "https://stackexchange.com/sites#science", "domain": "stackexchange.com"}, {"url": "https://meta.stackexchange.com", "domain": "meta.stackexchange.com"}, {"url": "https://stackapps.com", "domain": "stackapps.com"}, {"url": "https://api.stackexchange.com", "domain": "api.stackexchange.com"}, {"url": "https://data.stackexchange.com", "domain": "data.stackexchange.com"}, {"url": "https://area51.stackexchange.com", "domain": "area51.stackexchange.com"}, {"url": "https://stackoverflow.blog?blb=1", "domain": "stackoverflow.blog?blb=1"}, {"url": "https://www.facebook.com/officialstackoverflow/", "domain": "www.facebook.com"}, {"url": "https://twitter.com/stackoverflow", "domain": "twitter.com"}, {"url": "https://linkedin.com/company/stack-overflow", "domain": "linkedin.com"}, {"url": "https://creativecommons.org/licenses/by-sa/3.0/", "domain": "creativecommons.org"}, {"url": "https://stackoverflow.blog/2009/06/25/attribution-required/", "domain": "stackoverflow.blog"}], "domain": "stackoverflow.com"}, {"url": "https://www.linkedin.com/in/casadilla", "domain": "www.linkedin.com"}, {"url": "https://donoghuc.github.io", "children": [{"url": "https://www.cas-donoghue.org", "domain": "www.cas-donoghue.org"}, {"url": "https://www.linkedin.com/in/casadilla/", "domain": "www.linkedin.com"}, {"url": "https://github.com/donoghuc", "domain": "github.com"}, {"url": "https://stackoverflow.com/users/9034974/cas-donoghue?tab=profile", "domain": "stackoverflow.com"}, {"url": "https://www.cas-donoghue.org", "domain": "www.cas-donoghue.org"}, {"url": "https://talkpython.fm/", "domain": "talkpython.fm"}, {"url": "https://pythonbytes.fm/", "domain": "pythonbytes.fm"}, {"url": "https://www.podcastinit.com/", "domain": "www.podcastinit.com"}, {"url": "http://testandcode.com/", "domain": "testandcode.com"}, {"url": "https://changelog.com/", "domain": "changelog.com"}, {"url": "https://dataskeptic.com/", "domain": "dataskeptic.com"}, {"url": "https://www.dataengineeringpodcast.com/", "domain": "www.dataengineeringpodcast.com"}, {"url": "https://gimletmedia.com/science-vs/", "domain": "gimletmedia.com"}], "domain": "donoghuc.github.io"}], "domain": "www.cas-donoghue.org"}"""

        return {'crawl_result': graph}