document.getElementById('submitData').addEventListener('click', function() {
    fetch('/chart-data/')
    .then(response => response.json())
    .then(data => {
        // Update the chart with new data
        const chart = document.getElementById('pressureDepthChart').getContext('2d');
        const pressureDepthChart = new Chart(chart, {
            type: 'line',
            data: {
                labels: data.oil.depth,  // Depth labels
                datasets: [
                    {
                        label: 'Oil Pressure',
                        data: data.oil.pressure,
                        borderColor: 'green',
                        fill: false,
                    },
                    {
                        label: 'Gas Pressure',
                        data: data.gas.pressure,
                        borderColor: 'red',
                        fill: false,
                    },
                    {
                        label: 'Water Pressure',
                        data: data.water.pressure,
                        borderColor: 'blue',
                        fill: false,
                    },
                ]
            },
            options: {
                scales: {
                    x: { title: { display: true, text: 'Depth (ft)' } },
                    y: { title: { display: true, text: 'Pressure (psia)' } }
                }
            }
        });
    });
});
