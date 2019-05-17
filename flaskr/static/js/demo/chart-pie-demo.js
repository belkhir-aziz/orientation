// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';
var Arr = JSON.parse('{{ post | tojson }}');

 function occurence()   // declaration de la fonction avec un argument
{
var scores = new Array();
scores[0]=Arr[Informatique].length*2;
scores[0]=Arr[Télécommunication].length*2;
scores[0]=Arr[Indus].length*2;
scores[0]=Arr[Mécanique].length*2;
scores[0]=Arr[Electrique].length*2;
scores[0]=Arr[Civil].length*2;
return scores
}
alert(occurence());
// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Informatique", "Télécommunication", "Indus","Mécanique","Electrique","Civil"],
    datasets: [{
      data: occurence(),
      backgroundColor: ['#FA8072', '#FFFACD', '#7FFF00','	#00FFFF','#1E90FF','#DDA0DD'],
      hoverBackgroundColor: ['#B22222', '	#F0E68C', '	#008000','#40E0D0','#0000FF','	#BA55D3'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
