{% extends 'base.html' %}
{% load crispy_forms_tags %}
{% load static %}
{% block body %}
<style>
    *{
        margin:0;
        padding:0;
    }
    body{
        heigth: 100%;
        width:100%;
        bacground-repeat: no-repeat;
        background-position: center;
        background-size: cover;
        background-attachment: fixed;
    }
.card{
    width: 800px;
    heigth: 480px;
    position: center;
    margin: 5% 0 10% 35%;
    padding: 5px;
    background-color: rgba(0,0,0, 0.1);

}
</style>
<body style="background-image:url({% static 'Images/NewsImage.png'%})">
<div id="HTMLtoPDF">

//    <div id = "showData"></div>

</div>


<a href="#" onclick="HTMLtoPDF()" class="btn btn-primary">Download PDF</a>

<script src="{% static 'js/jquery-2.1.3.js' %}"></script>
<script src="{% static 'js/jspdf.js' %}"></script>
<script src="{% static 'js/pdfFromHTML.js' %}"></script>
//<script type = "text/javascript">
//    $(document).ready(function(){
//        $('#showData').load('report.html');
//    });
//</script>

</body>
{% endblock %}