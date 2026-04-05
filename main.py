with open('contact.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

self.wfile.write(html_content.encode('utf-8'))
