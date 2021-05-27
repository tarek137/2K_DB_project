<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">

        <html>

            <body>
                <h1> Films list :</h1>
                <ul>
                    <strong> <xsl:value-of select="/FILMS/FILM[9]/TITRE"  /></strong>
                    
                </ul>


            </body>

        </html>


    </xsl:template>

</xsl:stylesheet>

