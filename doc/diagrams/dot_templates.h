/****************
 *Node Templates*
 ****************/

#define STYLE_DEFAULT style="filled", fillcolor=lightgrey

#define UML_CLASS shape="plain", STYLE_DEFAULT
#define RECT shape="rect", STYLE_DEFAULT
#define CIRC shape="ellipse", STYLE_DEFAULT

/*************
 *HTML Tables*
 *************/
#define ROW(x)<tr>x</tr>
#define HEADER(x) ROW(<td><b>x</b></td>)


// Generate a non-outlined table. Pollute with <tr>s
#define SECTION(x)\
<tr><td>\
	<table border="0" cellborder="0" cellspacing="0">\
		x\
	</table>\
</td></tr>

// Generate a table with a header
#define TABLE(header, x)\
<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">\
	HEADER(header)\
	x\
</table>>


/*****
 *UML*
 *****/

// Generate a Row with a referencable port
#define UML_PROP(name, ref) <tr><td port=#ref align="left">name</td></tr>
