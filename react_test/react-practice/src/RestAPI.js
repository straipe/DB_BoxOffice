import React, { useState } from "react";
import axios from "axios";
import "./RestAPI.css";

function RestAPI(){
    const [text, setText] = useState([]);

    return (
        <>
            <h1>REST API Practice</h1>
            <div className="btn-primary">
                <button
                    onClick={()=>{
                        axios.post("http://127.0.0.1:8000/schedule/",{
                            // movno:"20230002",
                            // movname: "슈퍼마리오",
                            // runtimemin:92,
                            // certno:1,
                            // dirname:'아론 호바스',
                            // actname:'크리스 프렛, 안야 테일러 조이, 잭 블랙',
                            // movintro:"따단-딴-따단-딴 ? \n" +
                            // "전 세계를 열광시킬 올 타임 슈퍼 어드벤처의 등장! \n" +
                            // "뉴욕의 평범한 배관공 형제 '마리오'와 ‘루이지’는 배수관 고장으로 위기에 빠진 도시를 구하려다 미스터리한 초록색 파이프 안으로 빨려 들어가게 된다. \n"+
                            // "파이프를 통해 새로운 세상으로 차원 이동하게 된 형제. \n"+
                            // "형 '마리오'는 뛰어난 리더십을 지닌 '피치'가 통치하는 버섯왕국에 도착하지만 동생 '루이지'는 빌런 '쿠파'가 있는 다크랜드로 떨어지며 납치를 당하고\n"+
                            // "‘마리오’는 동생을 구하기 위해 ‘피치’와 ‘키노피오’의 도움을 받아 '쿠파'에 맞서기로 결심한다. \n"+
                            // "그러나 슈퍼스타로 세상을 지배하려는 그의 강력한 힘 앞에 이들은 예기치 못한 위험에 빠지게 되는데...!",
                            // distname:'유니버설 스튜디오',
                            // lang:'영어',
                            // imageurl:'https://github.com/wldnd9904/db_boxoffice/blob/master/frontend/images/posters/12323_222.jpg?raw=true',
                            // genno:4,
                            // release_date:'2023-04-26'
                            mov_no:6,
                            thea_no:1,
                            run_date: new Date('2023-05-27 10:10:00').toISOString().split('T')[0],
                            run_round: 1,
                            run_type: 1
                        }).then(function (response){
                            console.log(response);
                        }).catch(function(error){
                            console.log(error);
                        });
                    }}>
                        POST
                    </button>

                <button
                    onClick={()=>{
                        axios.get("http://127.0.0.1:8000/schedule/")
                        .then(function (response){
                            setText([...response.data]);
                        })
                        .catch(function(error){
                            console.log(error);
                        });
                    }}>
                        GET
                    </button>
                </div>   
                {text.map((e)=>(
                    <div>
                        {" "}
                        <div className="list">
                           <span>
                                {e.sched_no}번, {e.mov_no},{e.thea_no},{e.run_date},{e.run_round}
                            </span>
                            <button
                                className="btn-delete"
                                // onClick={()=>{
                                //     axios.delete(`http://127.0.0.1:8000/schedule/${e.movno}/`);
                                //     setText(text.filter((text)=> text.movno !== e.movno));
                                // }}
                                >
                                DELETE
                            </button>{" "}
                        </div>
                    </div>
                ))}  
        </>
    );
}

export default RestAPI;