# -*- coding: utf-8 -*-

from datetime import datetime, date, time


class Fields:
    pass
#TODO: check for bounding format in xml

def generateXml(Fields):
	fo = open(Fields.filename + '.xml', 'w')

	head = """<?xml version='1.0' encoding='UTF-8'?>
	<gmd:MD_Metadata xmlns:gmd='http://www.isotc211.org/2005/gmd'
	                 xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'
	                 xmlns:gml='http://www.opengis.net/gml'
	                 xmlns:gts='http://www.isotc211.org/2005/gts'
	                 xmlns:gco='http://www.isotc211.org/2005/gco'
	                 xmlns:geonet='http://www.fao.org/geonetwork'
	                 xmlns:csw='http://www.opengis.net/cat/csw/2.0.2'
	                 xsi:schemalocations='http://www.isotc211.org/2005/gmd http://www.isotc211.org/2005/gmd/gmd.xsd'>
	  <gmd:fileIdentifier>
	      <gco:CharacterString xmlns:srv='http://www.isotc211.org/2005/srv'
	                           xmlns:gmx='http://www.isotc211.org/2005/gmx'>394c47b6-acf6-4a8b-b53c-3367df06fd8c</gco:CharacterString>
	  </gmd:fileIdentifier>
	  <gmd:language>
	      <gco:CharacterString>"""+ Fields.language + """</gco:CharacterString>
	  </gmd:language>
	  <gmd:characterSet>
	      <gmd:MD_CharacterSetCode codeListValue='utf8'
	                               codeList='http://www.isotc211.org/2005/resources/codeList.xml#MD_CharacterSetCode'/>
	  </gmd:characterSet>
	  <gmd:contact>
	      <gmd:CI_ResponsibleParty>
	         <gmd:individualName>
	            <gco:CharacterString>Tatiana Semenova</gco:CharacterString>
	         </gmd:individualName>
	         <gmd:organisationName>
	            <gco:CharacterString>PICES</gco:CharacterString>
	         </gmd:organisationName>
	         <gmd:positionName>
	            <gco:CharacterString>Intern 2010-1011</gco:CharacterString>
	         </gmd:positionName>
	         <gmd:contactInfo>
	            <gmd:CI_Contact>
	               <gmd:phone>
	                  <gmd:CI_Telephone>
	                     <gmd:voice>
	                        <gco:CharacterString>+1-250-363-6366</gco:CharacterString>
	                     </gmd:voice>
	                     <gmd:facsimile>
	                        <gco:CharacterString>+1-250-363-6827</gco:CharacterString>
	                     </gmd:facsimile>
	                  </gmd:CI_Telephone>
	               </gmd:phone>
	               <gmd:address>
	                  <gmd:CI_Address>
	                     <gmd:deliveryPoint>
	                        <gco:CharacterString>9860 West Saanich Road</gco:CharacterString>
	                     </gmd:deliveryPoint>
	                     <gmd:city>
	                        <gco:CharacterString>Sidney</gco:CharacterString>
	                     </gmd:city>
	                     <gmd:administrativeArea>
	                        <gco:CharacterString>British Columbia</gco:CharacterString>
	                     </gmd:administrativeArea>
	                     <gmd:postalCode>
	                        <gco:CharacterString>V8L 4B2</gco:CharacterString>
	                     </gmd:postalCode>
	                     <gmd:country>
	                        <gco:CharacterString>Canada</gco:CharacterString>
	                     </gmd:country>
	                     <gmd:electronicMailAddress>
	                        <gco:CharacterString>tatiana@pices.int</gco:CharacterString>
	                     </gmd:electronicMailAddress>
	                  </gmd:CI_Address>
	               </gmd:address>
	            </gmd:CI_Contact>
	         </gmd:contactInfo>
	         <gmd:role>
	                     <gmd:CI_RoleCode codeListValue="pointOfContact"
	                             codeList="http://www.isotc211.org/2005/resources/codeList.xml#CI_RoleCode"/>
	         </gmd:role>
	      </gmd:CI_ResponsibleParty>
	  </gmd:contact>\n"""
	fo.write(head)



	#Вывод Current time

	fo.write("""  <gmd:dateStamp>
	      <gco:DateTime xmlns:srv="http://www.isotc211.org/2005/srv"
	                    xmlns:gmx="http://www.isotc211.org/2005/gmx">""" + str(datetime.today().date())
	                    + 'T'+ str(datetime.today().time())[ : 8] + """</gco:DateTime>
	  </gmd:dateStamp>\n""")

	#Xml standart

	fo.write("""  <gmd:metadataStandardName>
	      <gco:CharacterString xmlns:srv="http://www.isotc211.org/2005/srv"
	                           xmlns:gmx="http://www.isotc211.org/2005/gmx">ISO 19115:2003/19139</gco:CharacterString>
	  </gmd:metadataStandardName>
	  <gmd:metadataStandardVersion>
	      <gco:CharacterString xmlns:srv="http://www.isotc211.org/2005/srv"
	                           xmlns:gmx="http://www.isotc211.org/2005/gmx">1.0</gco:CharacterString>
	  </gmd:metadataStandardVersion>\n""") 



	#<gmd:identificationInfo>

	#title/publication date

	fo.write(""" 
	<gmd:identificationInfo>
	  <gmd:MD_DataIdentification>
		<gmd:citation>
	            <gmd:CI_Citation>
	               <gmd:title>
	                  <gco:CharacterString>""" + Fields.title + """</gco:CharacterString>
	               </gmd:title>
	               <gmd:date>
	                  <gmd:CI_Date>
	                     <gmd:date>
	                        <gco:DateTime>""" + Fields.pub_date + """</gco:DateTime>
	                     </gmd:date>
	                     <gmd:dateType>
	                        <gmd:CI_DateTypeCode codeListValue="publication"
	                                             codeList="http://www.isotc211.org/2005/resources/codeList.xml#CI_DateTypeCode"/>
	                     </gmd:dateType>
	                  </gmd:CI_Date>
	               </gmd:date>
	               <gmd:presentationForm>
	                  <gmd:CI_PresentationFormCode codeList="http://www.isotc211.org/2005/resources/codeList.xml#CI_PresentationFormCode"
	                                               codeListValue="documentDigital"/>
	               </gmd:presentationForm>
	               <gmd:presentationForm>
	                  <gmd:CI_PresentationFormCode codeList="http://www.isotc211.org/2005/resources/codeList.xml#CI_PresentationFormCode"
	                                               codeListValue="documentHardcopy"/>
	               </gmd:presentationForm>
	            </gmd:CI_Citation>
	         </gmd:citation>\n""")



	#abstract/purpose

	"""<gmd:abstract>
	            <gco:CharacterString>This is a final report (1993) of PICES Working Group 1. This report was written through the efforts of the Working Group 1 members.
	The northern North Pacific is a region of great biological abundance. Fisheries in the Bering Sea, Oyashio region and the Okhotsk Sea are among the most productive in the world. The biomass of the Okhotsk Sea rivals that of the Bering Sea. The "Oyashio" takes its name from its high productivity: parents (oya) current (shio) in Japanese. The
	Oyashio waters originate in the Okhotsk Sea and East Kamchatka Current, which is also the source of water for the Okhotsk Sea. However, the high oxygen and nutrient content of Oyashio and Okhotsk Water is not apparent in the East Kamchatka Current whose water is strongly modified in the Okhotsk Sea before it returns to the Oyashio.
	In this report, authors confined their attention to the hysical oceanographic aspects of the Okhotsk Sea and Oyashio area. The biological and chemical aspects of the region should be discussed at some point, but will not be reviewed by this PICES Working Group.</gco:CharacterString>
	         </gmd:abstract>
	         <gmd:purpose>
	            <gco:CharacterString>The objective of the report was to present a review of the importance of the Okhotsk Sea and Oyashio Region on the ventilation of the North Pacific Ocean, such as the formation of the North Pacific intermediate water.</gco:CharacterString>
	         </gmd:purpose>
	         <gmd:status>
	            <gmd:MD_ProgressCode codeListValue="completed"
	                                 codeList="http://www.isotc211.org/2005/resources/codeList.xml#MD_ProgressCode"/>
	         </gmd:status>"""



	#authors info

	for editor in Fields.editors:
	  fo.write("""         <gmd:pointOfContact>
	              <gmd:CI_ResponsibleParty>
	                 <gmd:individualName>
	                    <gco:CharacterString>""" + editor.name + """</gco:CharacterString>
	                 </gmd:individualName>\n""")
	  try:
	    fo.write("""              <gmd:organisationName>
	                    <gco:CharacterString>""" + editor.organisation + """</gco:CharacterString>
	                 </gmd:organisationName>\n""")
	  except Exception:
	    pass
	  fo.write("""               <gmd:contactInfo>
	                    <gmd:CI_Contact>
	                       <gmd:phone>
	                          <gmd:CI_Telephone>\n""")
	  try:
	    fo.write("""             <gmd:voice>
	                                <gco:CharacterString>""" + editor.phone + """</gco:CharacterString>
	                             </gmd:voice>\n""")
	  except Exception:
	    pass

	  try:
	    fo.write("""                             <gmd:facsimile>
	                                <gco:CharacterString>""" + editor.facs + """</gco:CharacterString>
	                             </gmd:facsimile>\n""")
	  except Exception:
	    pass
	                       
	  fo.write("""                       </gmd:CI_Telephone>
	                       </gmd:phone>
	                    <gmd:address>
	                          <gmd:CI_Address>\n""")

	  """                             <gmd:deliveryPoint>
	                                <gco:CharacterString>9500 Gilman Dr.</gco:CharacterString>
	                             </gmd:deliveryPoint>\n"""
	  try:                           
	    fo.write("""                           <gmd:city>
	                                  <gco:CharacterString>""" + editor.city + """</gco:CharacterString>
	                               </gmd:city>\n""")
	  except Exception:
	    pass
	  try:
	    fo.write("""                           <gmd:administrativeArea>
	                                <gco:CharacterString>""" + editor.area + """</gco:CharacterString>
	                             </gmd:administrativeArea>\n""")
	  except Exception:
	    pass
	  try:
	    fo.write("""                           <gmd:postalCode>
	                                <gco:CharacterString>""" + editor.postalCode + """</gco:CharacterString>
	                             </gmd:postalCode>\n""")
	  except Exception:
	    pass
	  try:  
	    fo.write("""                           <gmd:country>
	                                <gco:CharacterString>""" + editor.country + """</gco:CharacterString>
	                             </gmd:country>\n""")
	  except Exception:
	    pass
	  try:
	    fo.write("""                             <gmd:electronicMailAddress>
	                                  <gco:CharacterString>""" + editor.email + """</gco:CharacterString>
	                               </gmd:electronicMailAddress>\n""")
	  except Exception:
	    pass
	                          
	  fo.write("""                       </gmd:CI_Address>
	                        </gmd:address>
	                    </gmd:CI_Contact>
	                 </gmd:contactInfo>
	                 <gmd:role>
	                    <gmd:CI_RoleCode codeListValue="pointOfContact"
	                                     codeList="http://www.isotc211.org/2005/resources/codeList.xml#CI_RoleCode"/>
	                 </gmd:role>
	              </gmd:CI_ResponsibleParty>
	           </gmd:pointOfContact>
	        <gmd:resourceMaintenance>
	            <gmd:MD_MaintenanceInformation>
	               <gmd:maintenanceAndUpdateFrequency>
	                  <gmd:MD_MaintenanceFrequencyCode codeListValue="notPlanned"
	                                                   codeList="http://www.isotc211.org/2005/resources/codeList.xml#MD_MaintenanceFrequencyCode"/>
	               </gmd:maintenanceAndUpdateFrequency>
	            </gmd:MD_MaintenanceInformation>
	         </gmd:resourceMaintenance>\n""")


	#Graphics overview

	#Вывод keywords

	if Fields.keywords:
	  fo.write('\t<gmd:descriptiveKeywords>\n')
	  fo.write('\t\t<gmd:MD_Keywords>\n')

	  for key in Fields.keywords:
	    fo.write('\t\t\t<gmd:keyword>\n')
	    fo.write('\t\t\t\t<gco:CharacterString>'+ key + '</gco:CharacterString>\n')
	    fo.write('\t\t\t</gmd:keyword>\n')
	  fo.write("""      <gmd:type>
	                    <gmd:MD_KeywordTypeCode codeListValue="discipline"
	                                            codeList="http://www.isotc211.org/2005/resources/codeList.xml#MD_KeywordTypeCode"/>
	                 </gmd:type>
	              </gmd:MD_Keywords>
	           </gmd:descriptiveKeywords>\n""")


	if Fields.geo:
	  fo.write('\t<gmd:descriptiveKeywords>\n')
	  fo.write('\t\t<gmd:MD_Keywords>\n')

	  for key in Fields.geo:
	    fo.write('\t\t\t<gmd:keyword>\n')
	    fo.write('\t\t\t\t<gco:CharacterString>'+ key + '</gco:CharacterString>\n')
	    fo.write('\t\t\t</gmd:keyword>\n')
	  fo.write("""    <gmd:type>
	                    <gmd:MD_KeywordTypeCode codeListValue="place"
	                                            codeList="http://www.isotc211.org/2005/resources/codeList.xml#MD_KeywordTypeCode"/>
	                 </gmd:type>
	              </gmd:MD_Keywords>
	           </gmd:descriptiveKeywords>\n""")



	#Copyrights

	fo.write("""         <gmd:resourceConstraints>
	            <gmd:MD_LegalConstraints>
	               <gmd:accessConstraints>
	                  <gmd:MD_RestrictionCode codeListValue="copyright"
	                                          codeList="http://www.isotc211.org/2005/resources/codeList.xml#MD_RestrictionCode"/>
	               </gmd:accessConstraints>
	               <gmd:useConstraints>
	                  <gmd:MD_RestrictionCode codeListValue="copyright"
	                                          codeList="http://www.isotc211.org/2005/resources/codeList.xml#MD_RestrictionCode"/>
	               </gmd:useConstraints>
	            </gmd:MD_LegalConstraints>
	         </gmd:resourceConstraints>\n""")


	#TODO: this
	#Spatial resolutiom

	fo.write("""         <gmd:spatialResolution>
	            <gmd:MD_Resolution>
	               <gmd:equivalentScale>
	                  <gmd:MD_RepresentativeFraction>
	                     <gmd:denominator>
	                        <gco:Integer/>
	                     </gmd:denominator>
	                  </gmd:MD_RepresentativeFraction>
	               </gmd:equivalentScale>
	            </gmd:MD_Resolution>
	         </gmd:spatialResolution>\n""")



	#Language/encoding

	fo.write("""         <gmd:language>
	            <gco:CharacterString>eng</gco:CharacterString>
	         </gmd:language>
	         <gmd:characterSet>
	            <gmd:MD_CharacterSetCode codeListValue="utf8"
	                                     codeList="http://www.isotc211.org/2005/resources/codeList.xml#MD_CharacterSetCode"/>
	         </gmd:characterSet>\n""")


	#TODO: this
	#topicCategory

	fo.write("""         <gmd:topicCategory>
	            <gmd:MD_TopicCategoryCode>biota</gmd:MD_TopicCategoryCode>
	         </gmd:topicCategory>\n""")



	#Bounding boxes

	fo.write("""         <gmd:extent>
	            <gmd:EX_Extent>\n""")

	for location in Fields.locations:

	  fo.write("""               <gmd:geographicElement>
	                  <gmd:EX_GeographicBoundingBox>
	                     <gmd:westBoundLongitude>
	                        <gco:Decimal>""" + str(location[3]) + """</gco:Decimal>
	                     </gmd:westBoundLongitude>
	                     <gmd:eastBoundLongitude>
	                        <gco:Decimal>""" + str(location[2]) + """</gco:Decimal>
	                     </gmd:eastBoundLongitude>
	                     <gmd:southBoundLatitude>
	                        <gco:Decimal>""" + str(location[0]) + """</gco:Decimal>
	                     </gmd:southBoundLatitude>
	                     <gmd:northBoundLatitude>
	                        <gco:Decimal>""" + str(location[1]) + """</gco:Decimal>
	                     </gmd:northBoundLatitude>
	                  </gmd:EX_GeographicBoundingBox>
	               </gmd:geographicElement>\n""")

	fo.write("""            </gmd:EX_Extent>
	         </gmd:extent>
	         <gmd:supplementalInformation gco:nilReason="missing">
	            <gco:CharacterString/>
	         </gmd:supplementalInformation>
	      </gmd:MD_DataIdentification>
	  </gmd:identificationInfo>\n""")



	if Fields.url:
	  if 'PICES' in Fields.keywords:
	    description = "Whole document and separate articles in pdf at pices.int"
	  else:
	    description =  "document"
	  fo.write("""  <gmd:distributionInfo>
	      <gmd:MD_Distribution>
	         <gmd:transferOptions>
	            <gmd:MD_DigitalTransferOptions>
	                              <gmd:onLine>
	                  <gmd:CI_OnlineResource>
	                     <gmd:linkage>
	                        <gmd:URL>""" + Fields.url + """</gmd:URL>
	                     </gmd:linkage>
	                     <gmd:protocol>
	                        <gco:CharacterString>WWW:LINK-1.0-http--link</gco:CharacterString>
	                     </gmd:protocol>
	                     <gmd:name gco:nilReason="missing">
	                        <gco:CharacterString/>
	                     </gmd:name>
	                     <gmd:description>
	                        <gco:CharacterString>""" + description + """</gco:CharacterString>
	                     </gmd:description>
	                  </gmd:CI_OnlineResource>
	               </gmd:onLine>
	            </gmd:MD_DigitalTransferOptions>
	         </gmd:transferOptions>
	      </gmd:MD_Distribution>
	  </gmd:distributionInfo>\n""")

	fo.write("""</gmd:MD_Metadata>""")
	fo.close()