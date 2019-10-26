<template>
  <div class="hello">
    <h1>成績</h1>
    <vue-good-table
      class="stats-table"
      :columns="columns"
      :rows="rows">
    </vue-good-table>
    <router-link :to="{ path: '/' }">戻る</router-link>
  </div>
</template>

<script>
import BaseballClient from '../services/api';
export default {
  name: 'PitchingStats',
  data() {
    return {
      playerStats: null,
      columns: [
        {
          label: '選手名',
          field: 'prop',
        },
        {
          label: '',
          field: 'value',
        },
      ],
      rows: [
        {
          prop: '試合数',
          value: ''
        },
        {
          prop: '防御率',
          value: ''
        },
        {
          prop: '勝利数',
          value: ''
        },
        {
          prop: '敗戦数',
          value: ''
        },
        {
          prop: 'ホールドポイント',
          value: ''
        },
        {
          prop: 'セーブ',
          value: ''
        },
        {
          prop: '投球回',
          value: ''
        },
      ]
    }
  },
  methods: {
    async getStats() {
      const DataList = await BaseballClient.getFilteredPitchingStats({
        playerId: this.$route.params.playerId,
        year: 2018,
      });
      this.playerStats = DataList[0];
      this.columns[1].label = DataList[0].player.name;
      this.rows[0].value = DataList[0].game;
      this.rows[1].value = DataList[0].earnedRunAverage;
      this.rows[2].value = DataList[0].wins;
      this.rows[3].value = DataList[0].losses;
      this.rows[4].value = DataList[0].holdPoints;
      this.rows[5].value = DataList[0].saves;
      this.rows[6].value = DataList[0].inningsPitched;
    }
  },
  created() {
    this.getStats();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.stats-table {
  width: 50%;
  margin: 0 auto;
}
</style>
