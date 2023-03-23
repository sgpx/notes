# whatsapp

# reference

https://faq.whatsapp.com/425247423114725/?locale=en_US&cms_platform=iphone

# whatsapp URI

```
<html>
<body>
<button id="open-whatsapp">Open WhatsApp</button>
<script>

const myFunction = () => window.location.assign("whatsapp://send?text=hello%20from%20my%20webpage");
document.querySelector("#open-whatsapp").onclick = myFunction;
</script>
</body>
</html>
```
