import scrapy
from maangome.items import MaangomeItem


class MaangomeSpider(scrapy.Spider):
    name = "maangome"
    names = []
    details = []
    links = []

    def start_requests(self):
        urls = [
            'http://www.maango.me/hindi/page/1/',
            'http://www.maango.me/hindi/page/2/',
            'http://www.maango.me/hindi/page/3/',
            'http://www.maango.me/hindi/page/4/',
            'http://www.maango.me/hindi/page/5/',
            'http://www.maango.me/hindi/page/6/',
            'http://www.maango.me/hindi/page/7/',
            'http://www.maango.me/hindi/page/8/',
            'http://www.maango.me/hindi/page/9/',
            'http://www.maango.me/hindi/page/10/',
            'http://www.maango.me/malayalam/page/1/',
            'http://www.maango.me/malayalam/page/2/',
            'http://www.maango.me/malayalam/page/3/',
            'http://www.maango.me/malayalam/page/4/',
            'http://www.maango.me/malayalam/page/5/',
            'http://www.maango.me/malayalam/page/6/',
            'http://www.maango.me/malayalam/page/7/',
            'http://www.maango.me/malayalam/page/8/',
            'http://www.maango.me/malayalam/page/9/',
            'http://www.maango.me/malayalam/page/10/',
            'http://www.maango.me/malayalam/page/11/',
            'http://www.maango.me/tamil/page/1/',
            'http://www.maango.me/tamil/page/2/',
            'http://www.maango.me/tamil/page/3/',
            'http://www.maango.me/tamil/page/4/',
            'http://www.maango.me/tamil/page/5/',
            'http://www.maango.me/tamil/page/6/',
            'http://www.maango.me/tamil/page/7/',
            'http://www.maango.me/tamil/page/8/',
            'http://www.maango.me/tamil/page/9/',
            'http://www.maango.me/tamil/page/10/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = []
        albums = []
        result = []
        for play in response.css('a.play'):
            links.append(str(play.css('::attr(href)')[0].extract()))
            albums.append(str(play.css('::text')[0].extract()))

        for x in range(len(links)):
            result.append({'album': albums[x], 'link': links[x]})

        for page in result:
            # print page['album'], '\t\t\t\t', page['link']
            yield scrapy.Request(url=page['link'], callback=self.parse_song)

    def parse_song(self, response):

        print self.names, ' ', self.details, ' ', self.links
        self.title = str(response.css('div.p-info-serial span::text')[0].extract())
        print 'Album: ', self.title
        for songbox in response.css('div.songbox'):
            self.names.append(str(songbox.css('h2::text')[0].extract()))
            self.details.append(str(songbox.css('p::text')[0].extract()))
            self.links.append(str(songbox.css('div.songleft a::attr(href)')
                             .extract()[1]).replace(" ", "%20"))
            # print 'Song Name: ', name, '\nDetail: ', detail, '\nLink: ', link

        print '\n\n-----------------\n\n',self.title,self.names,self.details,self.links,'\n\n-------------------\n\n'
        item = MaangomeItem(album=self.title, tracks=self.names,
                            details=self.details, link=self.links)
        yield item
