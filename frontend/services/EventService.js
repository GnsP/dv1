import axios from 'axios'

const apiClient1 = axios.create({
    baseURL: 'http://localhost:8000/api',  //3000 earlier
    withCredentials: false,
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json' // double quote and single quotes r 
        //important in json 
    }
})

const apiClient2 = axios.create({
    baseURL: 'http://localhost:3001',
    withCredentials: false,
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
    }
})


export default {
    getEvents() {
        return apiClient1.get('/events')
    },
    getEvent(id) {
        return apiClient1.get('/events/' + id)
    },
    //------------------------//
    getArtists() {
        return apiClient2.get('/artists')
    },
    getArtist(id) {
    return apiClient2.get('/artists/' + id)
    }
}