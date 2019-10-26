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
  name: 'BattingStats',
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
          prop: '打率',
          value: ''
        },
        {
          prop: '本塁打',
          value: ''
        },
        {
          prop: '打点',
          value: ''
        },
        {
          prop: '出塁率',
          value: ''
        },
        {
          prop: '長打率',
          value: ''
        },
        {
          prop: 'OPS',
          value: ''
        },
        {
          prop: 'wOBA',
          value: ''
        },
      ]
    }
  },
  methods: {
    async getStats() {
      const DataList = await BaseballClient.getFilteredBattingStats({
        playerId: this.$route.params.playerId,
        year: 2018,
      });
      this.playerStats = DataList[0];
      this.columns[1].label = DataList[0].player.name;
      this.rows[0].value = DataList[0].avg;
      this.rows[1].value = DataList[0].homeRuns;
      this.rows[2].value = DataList[0].runsBattedIn;
      this.rows[3].value = DataList[0].onBasePercentage;
      this.rows[4].value = DataList[0].sluggingPercentage;
      this.rows[5].value = Number(DataList[0].onBasePercentage) + Number(DataList[0].sluggingPercentage);
      this.rows[6].value = this.calcWOBA(DataList[0]);
    },
    calcWOBA(data) {
      const walk = data.basesOnBalls;
      const intentionalWalk = data.intentionalWalk;
      const hitByPitch = data.hitByPitch;
      const singleHit = data.hits - data.twoBaseHits - data.threeBaseHits - data.homeRuns;
      const twoBaseHits = data.twoBaseHits;
      const threeBaseHits = data.threeBaseHits;
      const homeRuns = data.homeRuns;
      const atBats = data.atBats;
      const sacrificeFlies = data.sacrificeFlies;

      const wOBA = (0.69 * (walk - intentionalWalk) + 0.73 * hitByPitch + 0.87 * singleHit + 1.29 * twoBaseHits + 1.74 * threeBaseHits + 2.07 * homeRuns) / (atBats + walk - intentionalWalk + sacrificeFlies + hitByPitch);

      return Math.round(wOBA * 1000) / 1000;
    },
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
