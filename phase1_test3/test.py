import difflib

fc1 = 'abcd efgh'
fc2 = 'abc1 efg2'
html = []
outfile = open( 'difftest.html', 'w' )
for i in range(0,5):
    differ = difflib.HtmlDiff( tabsize=4, wrapcolumn=40 )
    html = (differ.make_file( fc1, fc2, context=False ))
    outfile.write(html)
outfile.close()