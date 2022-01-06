"""
Scrapy para recolher dados do site mercado livre:
Informacoes que seram "raspadas":

- Caixa de divisao de itens; sc-ctqQKy gLgKBM
- Nome do Produto; sc-kHOZwM brabbc sc-fHeRUh jwXwUJ nameCard
- Valor do Produtos; sc-iNGGcK fTkZBN priceCard selectorgadget_selected
"""
import scrapy


class CadeirasmlSpider(scrapy.Spider):
    name = 'cadeirasKabum'
    start_urls = ['https://www.kabum.com.br/computadores/notebooks-ultrabooks/notebooks?query=notebook&page_number=1&page_size=100&facet_filters=&sort=price']

    def parse(self, response):
        # Para cada nome dentro do loco do css aonde divide os itens, tra as infomacoes abaixo!
        for nome in response.css('sc-ctqQKy gLgKBM'):
            yield{
                'nome': nome.css('sc-kHOZwM brabbc sc-fHeRUh jwXwUJ nameCard::text').get(),
                'preco': nome.css('sc-iNGGcK fTkZBN priceCard selectorgadget_selected').get(),
            }
