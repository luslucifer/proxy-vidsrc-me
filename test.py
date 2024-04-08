
import requests
def fetch(url:str):
    host = 'fuck fuck'
    # url = request.args.get('url')  # Get the 'url' query parameter
    if url:
        res = requests.get(url)
        content = res.content
        text = res.text
        if url.replace(' ','').endswith('.m3u8'):
            print (' i am going to fuck you ')
            splited = text.splitlines()
            for index,line in enumerate(splited): 
                line = line.replace(' ', '')
                if line.startswith('https://'):
                    print(f'i am fine to {index} ')
                    splited[index]=f'http://{host}/fetch?url={line}'
            joined = '\n'.join(splited)
            return joined
        
        return content
    else:
        return 'No URL provided'

url = 'https://tmdrv.vidsrc.stream/stream/H4sIAAAAAAAAAw3K3W6CMBgA0Ff6gHWOXSp8ECKYlpZK7.jPBmtJmHGAPv1MzuWxQxzH1tg3.6ITTUz0oSNIiQb4OiTpZ_9jVs4rKnwoqN9PMo_2uliOPDmeGITLAIGquTu7eSPOI7SIJ.fTXwFIern0LbJCRfmDdhX2Ps3UE6_nOJV1pnqJ47st0tbMNlHyHri0icM60jM2_Do.tPAwzGZTz26zglEbloryrhMl3Xip6jYGGIANjOfESZxqxMoVcJMlExbDjefjXzN_EyGwsdO915zdWDZm1FdHNt2zi6xaV4qVedxNpHIWmsJJQl93NWUHyov1H4FYWYohAQAA/master.m3u8'

print(fetch(url))