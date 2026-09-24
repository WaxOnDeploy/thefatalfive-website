def head(title, desc, root="", extra=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/style.css">
{extra}
</head>
<body>
"""

def nav(root=""):
    return f"""<header class="site">
  <nav class="site">
    <a class="brand" href="{root}index.html">THE FATAL <span>FIVE</span></a>
    <ul class="navlinks" id="navlinks">
      <li><a href="{root}index.html#framework">Framework</a></li>
      <li><a href="{root}index.html#book">The Book</a></li>
      <li><a href="{root}corpus/index.html">The 65 Cases</a></li>
      <li><a href="{root}field-notes/index.html">Field Notes</a></li>
      <li><a href="{root}index.html#speaking">Speaking</a></li>
      <li><a href="{root}index.html#about">About</a></li>
    </ul>
    <button class="navtoggle" id="navtoggle" aria-label="Menu">&#9776;</button>
  </nav>
</header>
<script>
document.getElementById('navtoggle').addEventListener('click', function(){{
  document.getElementById('navlinks').classList.toggle('open');
}});
</script>
"""

def footer(root=""):
    return f"""<footer class="site">
  <div class="wrap">
    <div class="fbrand">THE FATAL FIVE &middot; Jeff Bourke</div>
    <div class="ftagline">The warnings are almost always there.</div>
    <ul class="flinks">
      <li><a href="{root}index.html#framework">Framework</a></li>
      <li><a href="{root}index.html#book">The Book</a></li>
      <li><a href="{root}corpus/index.html">The 65 Cases</a></li>
      <li><a href="{root}field-notes/index.html">Field Notes</a></li>
      <li><a href="{root}index.html#speaking">Speaking</a></li>
      <li><a href="{root}index.html#about">About</a></li>
      <li><a href="{root}index.html#contact">Contact</a></li>
    </ul>
    <div class="fbottom">
      <span>&copy; 2026 Jeff Bourke. All rights reserved.</span>
      <span>LinkedIn &middot; Email</span>
    </div>
  </div>
</footer>
</body>
</html>
"""
