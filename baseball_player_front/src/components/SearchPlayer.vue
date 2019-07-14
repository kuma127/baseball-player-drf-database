<template>
  <div class="hello">
    <h1>やきうの時間だあああああああ</h1>
    <div v-if="playerData">
      <router-link :to="{ path: '/stats/' + playerData.id }">{{ playerData.name }}</router-link>
      <label>チーム：{{ playerData.team }}  背番号：{{ playerData.no }}</label>
    </div>
    <label>1名検索！！！</label>
    <div class="inputData">
      <p>ID：</p><input type="number" v-model="playerId" min="0">
    </div>
    <button @click="testFunc">選手名表示</button>
    <br/>
    <label>複数検索！！！</label>
    <div class="inputData">
      <p>背番号：</p><input type="text" v-model="no">
    </div>
    <div class="inputData">
      <p>名前：</p><input v-model="name">
    </div>
    <div class="inputData">
      <p>チーム：</p>
      <select v-model="team">
        <option value="">Empty</option>
        <option v-for="option in teamList" v-bind:key="option" v-bind:value="option">
          {{ option }}
        </option>
      </select>
    </div>
    <div class="inputData">
      <button @click="searchPlayer">検索</button>
      <button @click="clearData">クリア</button>
    </div>
    <div v-for="pData in playerDataList" v-bind:key="pData.id">
      <router-link :to="{ path: '/stats/' + pData.id }">{{ pData.name }}</router-link>
      <label>チーム：{{ pData.team }}  背番号：{{ pData.no }}</label>
    </div>
  </div>
</template>

<script>
import BaseballClient from '../services/api';
export default {
  name: 'SearchPlayer',
  data() {
    return {
      playerData: null,
      playerDataList: [],
      playerId: 0,
      teamList: ['YS', 'YB', 'L', 'H'],
      no: '',
      name: '',
      team: '',
    }
  },
  methods: {
    async testFunc(){
      const response = await BaseballClient.getPlayerData(this.playerId);
      this.playerData = response;
    },
    async searchPlayer() {
      const response = await BaseballClient.getFilteredPlayerData({
        no: this.no,
        name: this.name,
        team: this.team
      });
      this.playerDataList = response;
    },
    clearData() {
      this.no = '';
      this.name = '';
      this.team = '';
      this.playerDataList = [];
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.inputData {
  display: flex;
  align-items: center;
  justify-content: center;
}
button {
  margin: .5em;
}
</style>
