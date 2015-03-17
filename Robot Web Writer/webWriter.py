from myro import *
init()

def avgLight():
    average = sum(getLight())/3.0
    return (average)

def makeWebpage():
    lightValues = []
    for item in range(9):
        p = takePicture()
        savePicture(p,"pic"+str(item)+".gif")
        lightValues.append( avgLight() )
        turnLeft(1,.5)

    
    f = open("myPage.html", "w")
    f.write("""
    <html>
    <head>Hi!!!!!!</head>
    <h1>Look at these pics!!!</h1>
    <body>
    <p>Produced by Dimond Gooden and Urkash Garg</p><br/>

    <table>
     <tr>
    <td><img src="pic0.gif" width="50%" height="25%" />"""
             + str(lightValues[0]) +
         """</td>    
    <td><img src="pic1.gif" width="50%" height="25%" />"""
             + str(lightValues[1]) +
         """</td>
    <td><img src="pic2.gif" width="50%" height="25%" />"""
             + str(lightValues[2]) +
      """</td>
      </tr>
      <tr>
        <td><img src="pic3.gif" width="50%" height="25%" />"""
             + str(lightValues[3]) +
      """</td>
          <td><img src="pic4.gif" width="50%" height="25%" />"""
             + str(lightValues[4]) +
      """</td>
          <td><img src="pic5.gif" width="50%" height="25%" />"""
             + str(lightValues[5]) +
      """</td>
      </tr>
      <tr>
          <td><img src="pic6.gif" width="50%" height="25%" />"""
             + str(lightValues[6]) +
      """</td>
          <td><img src="pic7.gif" width="50%" height="25%" />"""
             + str(lightValues[7]) +
      """</td>
          <td><img src="pic8.gif" width="50%" height="25%" />"""
             + str(lightValues[8]) +
      """</td>
      </tr>
    </table>
    <br/><p>Pictures taken by """+ getName()+"""</p>
    </body>
    </html>
    """)
 f.close()
