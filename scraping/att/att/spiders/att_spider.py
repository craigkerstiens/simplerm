from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import FormRequest, Request

class AttSpider(BaseSpider):
    name = "att"
    allowed_domains = ["att.com"]
    start_urls = ['https://www.att.com/olam/loginAction.olamexecute']
    
    def parse(self, response):
        return [FormRequest.from_response(response,
                    formdata={'wireless_num': '', 'pass': '', 'actionEvent': 'dotComLogin' },
                    callback=self.after_login)]

    def initial_login(self, response):
        return Request(url="https://www.att.com/olam/gotoDataDetailsAction.olamexecute?reportActionEvent=A_UMD_DATA_DETAILS",
            callback=self.parse_tastypage)
    
    def after_login(self, response):
        # check login succeed before going on
        return Request(url="https://www.att.com/olam/gotoDataDetailsAction.olamexecute?reportActionEvent=A_UMD_DATA_DETAILS",
            callback=self.parse_tastypage)
        print 'loggedin'
    
    def parse_tastypage(self, response):
        hxs = HtmlXPathSelector(response)
        print '--------------------------------------'
        print hxs.select('//title').extract()
        print '--------------------------------------'
        from scrapy.shell import inspect_response
        inspect_response(response)
        #print '--------------------------------------'
        #print hxs.select("//div[@class='botMar10']").extract()
        #for row in hxs.select('//table//tbody//tr'):
        #    print row.select('//td').extract()
        #print '--------------------------------------'
    
    
    
