# Let's see if it's even remotely reasonable to actually put
# all of this in color on a webpage.

import re

lines = []
with open("wilderness.txt") as f:
    lines = f.readlines()

html = []
html.append('<html><head><title>Lensmoor Wilderness Map</title><link rel="stylesheet" href="wilderness.css"></head><body>\n')
for line in lines:
    # WARNING: Because of the risk of replacing things that
    # we've introduced to a string through *other* replacements,
    # everything in this sequence must be done in a VERY
    # particular order. If you change this at all, you need to
    # know exactly what you're doing, or you'll have some bugs
    # that will probably be difficult to track down!

    # First, convert numbers to placeholder letters that we're not
    # using anywhere else - this is to prevent conflicts with
    # replacing HTML codes.
    #
    # Potentially, I could have avoided having to do this part
    # by just making the roads into letters to begin with, but
    # I think the numbers are a bit easier to visually pick out
    # than the letters are when reading the raw text. For this
    # reason, I decided to leave them as numbers in the text.

    line = re.sub('1', 'A', line)
    line = re.sub('2', 'B', line)
    line = re.sub('3', 'C', line)
    line = re.sub('4', 'D', line)
    line = re.sub('5', 'E', line)

    # Convert all desert tiles into HTML codes right off the bat. Since
    # HTML codes themselves have a semicolon in them, we need to do
    # this replacement early - but not before the above. Since there's
    # a 5 in this HTML character code, we need to do the above subs
    # first, otherwise we'd be replacing the 5 here with E.
    #
    # Also convert all forest tiles into HTML codes. Since we've
    # already put some extra pound signs into the document, we
    # need to make sure we don't catch any instances that aren't
    # preceded with an ampersand.
    #
    # Finally, convert all swamp tiles into HTML codes as well.
    
    line = re.sub(';', '&#59;', line)
    line = re.sub('([^&])#', '\g<1>&#35;', line)
    line = re.sub('([^&])#', '\g<1>&#35;', line)
    line = re.sub('"', '&#35;', line)
    line = re.sub('\*', '&#42;', line)

    # Temporarily turn all backslashes into percent signs, to
    # prevent escape issues from happening. Later we'll turn
    # the percent signs back into blue backslashes, but we need
    # to turn the letter 'D' into white backslashes first.
    #
    # Also take the lowercase wilderness tiles and turn them
    # into codes. This is to prevent conflicts with the span
    # tag replacements.

    line = re.sub('\\\\','&#37;',line)
    line = re.sub('0', '&#48;', line)
    line = re.sub('n', '&#110;', line)
    line = re.sub('o', '&#111;', line)

    # Now we turn all the road letters into their respective road
    # tiles.
    line = re.sub('A', '&#43;', line)
    line = re.sub('B', '&#45;', line)
    line = re.sub('C', '&#124;', line)
    line = re.sub('D', '&#92;', line)
    line = re.sub('E', '&#47;', line)

    line = re.sub('((&#43;)+)', '<span class="road">\g<1></span>', line)
    line = re.sub('((&#45;)+)', '<span class="road">\g<1></span>', line)
    line = re.sub('((&#124;)+)', '<span class="road">\g<1></span>', line)
    line = re.sub('((&#92;)+)', '<span class="road">\g<1></span>', line)
    line = re.sub('((&#47;)+)', '<span class="road">\g<1></span>', line)
    
    # We're done with roads - now we'll do rivers.

    line = re.sub('(\++)','<span class="river">\g<1></span>',line)
    line = re.sub('(\-+)','<span class="river">\g<1></span>',line)
    line = re.sub('(\|+)','<span class="river">\g<1></span>',line)
    line = re.sub('((&#37;)+)','<span class="river">\g<1></span>',line)

    # This last one captures and prints back two groups because we need
    # to make sure we're not catching forward slashes that are part of
    # a closing HTML tag.
    line = re.sub('([^<])(\/+)','\g<1><span class="river">\g<2></span>',line)
    
    # Finally, we convert the percent signs back into backslashes.
    line = re.sub('&#37;','&#92;',line)
    
    line = re.sub('(\^+)','<span class="mountains">\g<1></span>',line)
    line = re.sub('((&#59;)+)','<span class="desert">\g<1></span>',line)
    line = re.sub('(I+)','<span class="tundra">\g<1></span>',line)
    line = re.sub('(O+)','<span class="water">\g<1></span>',line)
    line = re.sub('((&#35;)+)','<span class="forest">\g<1></span>',line)
    line = re.sub('((&#110;)+)','<span class="hills">\g<1></span>',line)
    line = re.sub('((&#111;)+)','<span class="ocean">\g<1></span>',line)
    line = re.sub('(\.+)','<span class="plains">\g<1></span>',line)
    line = re.sub('((&#48;)+)','<span class="deepwater">\g<1></span>',line)
    line = re.sub('((&#35;)+)','<span class="swamp">\g<1></span>',line)
    line = re.sub('((&#42;)+)','<span class="city">\g<1></span>',line)
    line = re.sub('(V+)','<span class="vehicle">\g<1></span>',line)

    line = re.sub('\n', '<br>\n',line)
    html.append(line)
    continue
    line = line + "<br>"
    html.append(line)
html.append("</body></html>")

outfile = open("wilderness.html", "w")
outfile.writelines(html)
outfile.close()