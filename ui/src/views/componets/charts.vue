
<template>
    <div ref="lineChart" id="line-chart"></div>
</template>
<script>
import Echarts from 'echarts'
export default {
    data() {
        return{
            myChart: {},
            option: {
                legend: {
                    bottom: 1
                },
                title: {
                    // text: this.data.title.text
                    text: '每月新增主机数量',
                    fontSize: 12,
                    textStyle: {
                        fontSize: 16,
                        color: '#24292E'
                    },
                    padding: 20
                },
                tooltip: {},
                xAxis: {
                    // data: this.data.xAxis.data
                    type: 'category',
                    boundaryGap: false,
                    axisLine: {
                        onZero: false,
                        lineStyle: {
                            color: '#23282C'
                        }
                    },
                    data: this.xdata
                },
                yAxis: {
                    type: 'value',
                    axisLine: {
                        onZero: false,
                        lineStyle: {
                            color: '#23282C'
                        }
                    },
                    splitLine: { //网格线
                        show: false
                    }
                },
                series: {
                    data: [213, 342, 34, 5, 24, 24, 131, 131, 131, 131, 131, 142],
                    type: 'line',
                    itemStyle: {
                        normal: {
                            color: '#fff',
                            borderColor: '#4bc8db',
                            areaStyle: {
                                type: 'default',
                                opacity: 0.4
                            }
                        }
                    },
                    lineStyle: {
                        // 线性渐变，前四个参数分别是 x0, y0, x2, y2, 范围从 0 - 1，相当于在图形包围盒中的百分比，如果 globalCoord 为 `true`，则该四个值是绝对的像素位置
                        color: '#4D73BE'
                    },
                }
            },
            default() {
                return {};
            }
        }
    },
    props: {
        data: {
            type: Object,
        }
    },
    created() {
        let xData = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'];
            const today = new Date();
            let month = today.getMonth();
            console.log(xData.length)
            for (let i = 0; i < xData.length; i++) {
                if (i === month) {
                    xData.splice(0, xData.length, ...xData.slice(i + 1, xData.length).concat(...xData.slice(0, i + 1)))
                }
            }
        this.chooseAPI(this.data.title).then(res => {
                if (res.result) {
                    this.option.xAxis.data = xData
                    this.option.series.data = res.series
                    this.$nextTick(() => {
                        this.loadEchart()
                    })
                } else {
                    this.$message.error(res.message)
                }
            })
    },
    watch: {
        data: {
            handler () {
            if (this.myChart.id) this.myChart.resize()
            },
            deep: true
        },
        'this.$store.state.home.homeState' () {
            if (this.myChart.id) this.myChart.resize()
        }
    },
    mounted() {
    },
    methods: {
        chooseAPI (title) {
            this.option.title.text = title
            switch (title) {
                case '每月新增主机数量':
                    return this.$api.Home.GetHostNumVerMonth()
                case '每月执行任务频率(作业平台)':
                    return this.$api.Home.GetJobNumVerMonth()
                case '每月执行任务频率(标准运维)':
                    return this.$api.Home.GetSopNumVerMonth()
            }
        },
        loadEchart() {
            this.myChart = Echarts.init(this.$refs.lineChart);
            this.myChart.setOption(this.option)
        }
    }
}
</script>
<style>
#line-chart{
    height: 100%;
}
</style>
