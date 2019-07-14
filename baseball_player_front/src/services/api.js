import axios from 'axios';
import {loadProgressBar} from 'axios-progress-bar';
import camelcaseKeys from 'camelcase-keys';


const _handleSuccess = response => {
    // 全てのJSONのキーをスネークケースからキャメルケースに変換する
    response.data = camelcaseKeys(response.data, { deep: true });
    return response;
};

class Client {
    constructor() {
        this.service = axios.create();
        this.service.interceptors.response.use(_handleSuccess);
        loadProgressBar({ showSpinner: false }, this.service);
    }

    _get(path, payload) {
        return this.service.get(path, payload);
    }

    _patch(path, payload) {
        return this.service.patch(path, payload);
    }

    _post(path, payload, config={}) {
        return this.service.post(path, payload, config);
    }

    _put(path, payload) {
        return this.service.put(path, payload);
    }

    _delete(path) {
        this.service.delete(path);
    }

}

class BaseballClient extends Client {
    constructor() {
        super();
        this.baseUrl = 'http://localhost:8000/api';
    }

    async getPlayerList() {
        const response = await this._get(`${this.baseUrl}/players/`);
        return response.data;
    }

    async getPlayerData(playerId) {
        const response = await this._get(`${this.baseUrl}/players/${playerId}/`);
        return response.data;
    }

    async getFilteredPlayerData({no, name, team}) {
        const response = await this._get(`${this.baseUrl}/players/?no=${no}&name=${name}&team=${team}`);
        return response.data;
    }

    async getFilteredPlayerStats({playerId, year}) {
        const response = await this._get(`${this.baseUrl}/batting-stats/?player=${playerId}&year=${year}&player__name=`);
        return response.data;
    }
}

export default new BaseballClient();