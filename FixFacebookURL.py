# Title: Replace facebook.com url, which should be workplace.com

try:
    originaluri = document.get_meta_data_value("originaluri")[-1]
    clickableuri = document.get_meta_data_value("clickableuri")[-1]
    printableuri= document.get_meta_data_value("printableuri")[-1]
    uri = document.uri
    document.add_meta_data(
        {"originaluri": originaluri.replace("facebook.com", "workplace.com")})
    document.add_meta_data(
        {"clickableuri": clickableuri.replace("facebook.com", "workplace.com")})
    document.add_meta_data(
        {"printableuri": printableuri.replace("facebook.com", "workplace.com")})
    document.uri = uri.replace("facebook.com", "workplace.com")
except Exception as e:
    log(str(e))

# Fix Title on Comments

try:
    meta_title = document.get_meta_data_value("title")
    if not meta_title:
      #title = meta_title[-1]
      #if ("https://" in title):
         meta = document.get_meta_data_value("mymessage")
         if (len(meta)>0):
           log('mymessage: '+meta[-1])
           document.add_meta_data({"title": meta[-1]})
         else:
           meta = document.get_meta_data_value("mystory")
           if (len(meta)>0):
             log('mystory: '+meta[-1])
             document.add_meta_data({"title": meta[-1]})

except Exception as e:
    log(str(e))
