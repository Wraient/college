#include &lt;graphics.h&gt;
#include&lt;iostream&gt;
#include &lt;math.h&gt;
using namespace std;
void drawline(int x1,int y1,int x2,int y2)
{
int dx,dy,m,s;
float xi,yi,x,y;
dx = x2 - x1;
dy = y2 - y1;
if (abs(dx) &gt; abs(dy))
s = abs(dx);
else
s = abs(dy);

xi = dx / (float) s;
yi = dy / (float) s;
x = x1;
y = y1;
putpixel(x1, y1, WHITE);
for (m = 0; m &lt; s; m++)
{
putpixel(x, y, WHITE);
x += xi;
y += yi;
}
delay(500);
}
int main()
{
int gd=DETECT, gm=DETECT,x1,y1,x2,y2;

initgraph(&amp;gd,&amp;gm,NULL);
drawline(100,200,300,350);
closegraph();
}