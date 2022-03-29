(function init () {
    const data = JSON.parse(
        document.getElementById("graphData").getAttribute("data-graph")
    );

    console.log(data);

    var tempSeries = [];
    var humSeries = [];
    var rainSeries = [];
    for(var i = 0; i < data.logtime.length; i++) {
        const currDate = new Date(data.logtime[i]).getTime();

        tempSeries.push({
            x: currDate,
            y: data.temperature[i]
        })

        humSeries.push({
            x: currDate,
            y: data.humidity[i]
        })

        rainSeries.push({
            x: currDate,
            y: data.rains[i]
        })
    }

    const series = [
        {
            name: "Temperature",
            data: tempSeries
        },
        {
            name: "Humidity",
            data: humSeries
        },
        {
            name: "Rain",
            data: rainSeries
        }
    ]

    var options = {
        chart: {
            type: 'line',
            height: 400,
            sparkline: {
                enabled: true,
            }
        },
        colors: ['#77B6EA', '#545454', '#FF0000'],
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: 'smooth'
        },
        title: {
          text: 'Weather Data',
          align: 'center'
        },
        markers: {
          size: 1
        },
        xaxis: {
            type: 'datetime',
            title: {
                text: "TimeStamp"
            } 
        },
        yaxis: {
            title: {
                text: "Temp/Humidity/Rain Values"
            }
        },
        legend: {
          position: 'top',
          horizontalAlign: 'right',
          floating: true,
          offsetY: -25,
          offsetX: -5
        },
        series: series
    }

    console.log(options)

    var chart = new ApexCharts(document.getElementById("weatherChart"), options);
    chart.render();

})()